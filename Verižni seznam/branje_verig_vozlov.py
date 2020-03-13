# =============================================================================
# Branje verig vozlov
#
# Za spodnje naloge morate uvoziti vse definicije iz naloge _Veriga vozlov_.
# To storite z:
# 
#     from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama
# =====================================================================@022433=
# 1. podnaloga
# Sestavite funkcijo `dolzina(prvi)`, ki vrne število vozlov v verigi vozlov,
# ki se začne z vozlom `prvi`. Zgled:
# 
#     >>> v = Vozel('sobota')
#     >>> v = dodaj_na_konec(v, 'nedelja')
#     >>> v = dodaj_na_zacetek(v, 'petek')
#     >>> dolzina(v)
#     3
# =============================================================================
from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama

class Vozel(Vozel):
    def dolzina(prvi):
        '''vrne stevilo vozlov v verigi, ki se zacne s prvim'''
        vozel = prvi
        stevec = 0
        while vozel is not None:
            stevec += 1
        return stevec
# =====================================================================@022434=
# 2. podnaloga
# Sestavite funkcijo `zadnji_vozel(prvi)`, ki vrne referenco na
# zadnji vozel v verigi vozlov, ki se začne z vozlom `prvi`. Zgled:
# 
#     >>> v = iz_seznama(['sreda', 'četrtek', 'petek', 'sobota'])
#     >>> zadnji_vozel(v).podatek
#     'sobota'
# =============================================================================
class Vozel(Vozel):
    def zadnji_vozel(prvi):
        while prvi.naslednji is not None:
            prvi = prvi.naslednji
        return prvi

# =====================================================================@022435=
# 3. podnaloga
# Sestavite funkcijo `seznam_sodih(prvi)`, ki vrne seznam vseh sodih elementov
# v verigi vozlov, ki se začne z vozlom `prvi`. Predpostavite lahko, da so vsi
# podatki cela števila. Zgled:
# 
#     >>> v = iz_seznama([3, 4, 5, 6, 7, 8, 9, 10, 11])
#     >>> seznam_sodih(v)
#     [4, 6, 8, 10]
# =============================================================================

# =====================================================================@022436=
# 4. podnaloga
# Sestavite funkcijo `pogojni_seznam(prvi, pogoj)`, ki kot argument dobil
# verigo vozlov, ki se začne z vozlom `prvi`, ter funkcijo `pogoj`, ki sprejme
# en element in vrne logično vrednost. Funkcija `pogojni_seznam` naj sestavi
# in vrne seznam vseh podatkov, pri katerih funkcija `pogoj` vrne `True`. Zgled:
# 
#     >>> v = iz_seznama(['sreda', 'četrtek', 'petek', 'sobota'])
#     >>> pogojni_seznam(v, lambda s: s.endswith('ek'))
#     ['četrtek', 'petek']
# =============================================================================

# =====================================================================@022437=
# 5. podnaloga
# Sestavite funkcijo `je_urejen(prvi)`, ki vrne `True`, če so podatki v verigi
# vozlov urejeni naraščajoče in `False`, če niso. Zgled:
# 
#     >>> v = iz_seznama([1, 2, 4, 7, 8])
#     >>> je_urejen(v)
#     True
#     >>> v = iz_seznama([1, 2, 4, 3, 7])
#     >>> je_urejen(v)
#     False
# =============================================================================





































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import json, os, re, sys, shutil, traceback, urllib.error, urllib.request


import io, sys
from contextlib import contextmanager

class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end='')
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end='')
        return line


class Check:
    parts = None
    current_part = None
    part_counter = None

    @staticmethod
    def has_solution(part):
        return part['solution'].strip() != ''

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['valid'] = True
            part['feedback'] = []
            part['secret'] = []

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part['feedback'].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part['valid'] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed))
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted([(Check.clean(k, digits, typed), Check.clean(v, digits, typed)) for (k, v) in x.items()])
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get('clean', clean)
        Check.current_part['secret'].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error('Izraz {0} vrne {1!r} namesto {2!r}.',
                        expression, actual_result, expected_result)
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error('Namestiti morate numpy.')
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error('Ta funkcija je namenjena testiranju za tip np.ndarray.')

        if env is None:
            env = dict()
        env.update({'np': np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error("Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                        type(expected_result).__name__, type(actual_result).__name__)
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error("Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.", exp_shape, act_shape)
            return False
        try:
            np.testing.assert_allclose(expected_result, actual_result, atol=tol, rtol=tol)
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        exec(code, global_env)
        errors = []
        for (x, v) in expected_state.items():
            if x not in global_env:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(global_env[x]) != clean(v):
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, global_env[x], v))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', statements,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, 'w', encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part['feedback'][:]
        yield
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n    '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}', filename, '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part['feedback'][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get('stringio')('\n'.join(content) + '\n')
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n  '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}', '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error('Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            exec(expression, global_env)
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal:
            return True
        else:
            Check.error('Program izpiše{0}  namesto:\n  {1}', (line_width - 13) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ['\n']
        else:
            expected_lines += (actual_len - expected_len) * ['\n']
        equal = True
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['Program izpiše'])
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append('{0} {1} {2}'.format(out.ljust(line_width), '|' if out == given else '*', given))
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get('update_env', update_env):
            global_env = dict(global_env)
        global_env.update(Check.get('env', env))
        return global_env

    @staticmethod
    def generator(expression, expected_values, should_stop=None, further_iter=None, clean=None, env=None, update_env=None):
        from types import GeneratorType
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error("Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                                iteration, expression, actual_value, expected_value)
                    return False
            for _ in range(Check.get('further_iter', further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False
        
        if Check.get('should_stop', should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print('{0}. podnaloga je brez rešitve.'.format(i + 1))
            elif not part['valid']:
                print('{0}. podnaloga nima veljavne rešitve.'.format(i + 1))
            else:
                print('{0}. podnaloga ima veljavno rešitev.'.format(i + 1))
            for message in part['feedback']:
                print('  - {0}'.format('\n    '.join(message.splitlines())))

    settings_stack = [{
        'clean': clean.__func__,
        'encoding': None,
        'env': {},
        'further_iter': 0,
        'should_stop': False,
        'stringio': VisibleStringIO,
        'update_env': False,
    }]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs))
                             if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get('env'))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get('stringio'):
            yield
        else:
            with Check.set(stringio=stringio):
                yield


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\s*\n' # beginning of header
            r'(\s*#( [^\n]*)?\n)+?'     # description
            r'\s*# =+\s*?\n'            # end of header
            r'(?P<solution>.*?)'        # solution
            r'(?=\n\s*# =+@)',          # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                if 'token' in part:
                    submitted_part['token'] = part['token']
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        request = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoxNjYwLCJwYXJ0IjoyMjQzM30:1iRgXq:9rqW0sb1Muqp1CVttM8bMoJ60Rs'
        try:
            test_data = [
                (["n = dolzina(None)"],
                 {'n': 0}),
                (["v = Vozel(3)",
                  "v = dodaj_na_konec(v, 2)",
                  "n = dolzina(v)"],
                 {'n': 2}),
                (["v = Vozel('petek')",
                  "v = dodaj_na_konec(v, 'sobota')",
                  "v = dodaj_na_konec(v, 'nedelja')",
                  "n = dolzina(v)"],
                 {'n': 3}),
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoxNjYwLCJwYXJ0IjoyMjQzNH0:1iRgXq:A_Q4WQHUt6pCokLRQ2XlPKsarME'
        try:
            test_data = [
                (["v = iz_seznama(['sreda', 'četrtek', 'petek', 'sobota'])",
                  "nasl = zadnji_vozel(v).naslednji",
                  "data = zadnji_vozel(v).podatek"],
                 {'nasl': None, 'data': 'sobota'}),
                (["v = iz_seznama([2, 3, 4, 5, 6, 7, 8, 9])",
                  "nasl = zadnji_vozel(v).naslednji",
                  "data = zadnji_vozel(v).podatek"],
                 {'nasl': None, 'data': 9}),
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
            Check.equal('zadnji_vozel(iz_seznama([]))', None)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoxNjYwLCJwYXJ0IjoyMjQzNX0:1iRgXq:3LPosoroEEpmANorD4cEO_BAfXU'
        try:
            test_data = [
                ('seznam_sodih(None)', []),
                ('seznam_sodih(iz_seznama([3, 4, 5, 6, 7]))', [4, 6]),
                ('seznam_sodih(iz_seznama([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))', [2, 4, 6, 8, 10]),
                ('seznam_sodih(iz_seznama([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))', [2, 4, 6, 8, 10, 12]),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoxNjYwLCJwYXJ0IjoyMjQzNn0:1iRgXq:ZFG8G7NlQu2_H-oTMicvYYh7TRc'
        try:
            test_data = [
                (["v = iz_seznama(['sreda', 'četrtek', 'petek', 'sobota'])",
                  "l = pogojni_seznam(v, lambda s: s.endswith('ek'))"],
                 {'l': ['četrtek', 'petek']}),
                (["v = iz_seznama([2, 3, 4, 5, 6, 7, 8, 9])",
                  "l = pogojni_seznam(v, lambda x: 3 <= x <= 7)"],
                 {'l': [3, 4, 5, 6, 7]}),
                (["v = iz_seznama(['sreda', 'četrtek', 'petek', 'sobota'])",
                  "l = pogojni_seznam(v, lambda s: True)"],
                 {'l': ['sreda', 'četrtek', 'petek', 'sobota']}),
                (["v = iz_seznama([2, 3, 4, 5, 6, 7, 8, 9])",
                  "l = pogojni_seznam(v, lambda x: 30 <= x)"],
                 {'l': []}),
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoxNjYwLCJwYXJ0IjoyMjQzN30:1iRgXq:C-XUa05LZvI7NRdab4A23kMY7pc'
        try:
            test_data = [
                ("je_urejen(iz_seznama([]))", True),
                ("je_urejen(iz_seznama([1, 2, 4, 7, 8]))", True),
                ("je_urejen(iz_seznama([1, 2, 4, 3, 7, 8]))", False),
                ("je_urejen(iz_seznama(['ananas', 'banana', 'lubenica', 'pomaranča']))", True),
                ("je_urejen(iz_seznama(['ananas', 'banana', 'pomaranča', 'lubenica']))", False),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token 93e2980890f94e76227c9998864eb216eb497cdb'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        print('PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE! Poskusite znova.')
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print('Posodabljam datoteko... ', end="")
            backup_filename = backup(filename)
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(response['update'])
            print('Stara datoteka je bila preimenovana v {0}.'.format(backup_filename))
            print('Če se datoteka v urejevalniku ni osvežila, jo zaprite ter ponovno odprite.')
    Check.summarize()

if __name__ == '__main__':
    _validate_current_file()
