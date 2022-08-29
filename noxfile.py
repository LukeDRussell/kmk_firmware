import nox
import shutil
from pathlib import Path

source_dir = Path('kmk')
build_dir = Path('build')

py_ver_tested = ['3.9', '3.10', '3.11']

black_ver_tested = ['21.6b0', '22.6.0']

@nox.session(python=py_ver_tested)
@nox.parametrize('black_ver', black_ver_tested)
def black(session,black_ver):
    '''Format python code with `black`.'''
    session.install(f'black=={black_ver}')
    session.run('black', f'{source_dir}')


@nox.session(python=py_ver_tested[0])
def isort(session):
    session.install('isort')
    session.run('isort', f'{source_dir}')


@nox.session(python=py_ver_tested[0])
def flake8(session):
    session.install('flake8')
    session.run('flake8', f'{source_dir}')


@nox.session(python=py_ver_tested[0])
def clean(session):
    build_dir.mkdir(exist_ok=True)
    for child in build_dir.iterdir():
        if child.is_file():
            child.unlink()
        else:
            shutil.rmtree(child)


@nox.session(python=py_ver_tested[0])
def compile(session):

    clean(session)

    shutil.copy2('boot.py', 'build/boot.py')

    # Make sure the full folder heirarchy exists
    for d in source_dir.glob('**/'):
        if not build_dir.joinpath(d).exists():
            Path.mkdir(build_dir.joinpath(d))

    # Compile every python file
    for x in source_dir.glob('**/*.py'):
        out_path = str(build_dir.joinpath(x).with_suffix('.mpy'))
        session.run('mpy-cross', f'{x}', '-o', f'{out_path}', external=True)

@nox.session(python=py_ver_tested)
def bump_py_ver(session):
    flake8(session)
    isort(session)
    black(session, black_ver_tested)
    compile(session)

nox.options.sessions = ['black', 'isort', 'flake8']  # Default sessions
