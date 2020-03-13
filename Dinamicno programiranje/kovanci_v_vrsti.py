# =============================================================================
# Kovanci v vrsti
# =====================================================================@023289=
# 1. podnaloga
# Čestitam! V nagradni igri si bil izžreban za dobitnika nagrade. Kolikšna bo
# nagrada, pa je odvisno od tvoje iznajdljivosti. Za nagrado si lahko izbereš
# poljubne kovance iz podane vrste kovancev (ki so lahko vsi različni ali pa
# tudi ne). Edini pogoj pri izbiranju je, da nikoli ne izbereš dveh
# sosednjih kovancev. Da se boš prepričal, da si boš izbral največjo možno
# nagrado, sestavi funkcijo `nagrada(kovanci)`, ki bo za dane kovance vrnila
# največjo možno vsoto, ki jo lahko izbereš.
# 
#     >>> nagrada([5, 6, 4, 8, 1, 2, 1, 1])
#     17
#     >>> nagrada([2, 2, 2])
#     4
#     >>> nagrada([1, 3, 1])
#     3
#     >>> nagrada([1, 3, 1, 4, 6])
#     9
#     >>> nagrada([3, 2, 1, 4, 6])
#     10
#     >>> nagrada([10, 2, 8, 16, 14, 2, 10, 4, 5, 7])
#     49
#     >>> nagrada([10, 2, 8, 16, 14, 10, 4, 5, 7])
#     43
# =============================================================================
def nagrada(kovanci):
    ''' Za dane kovance vrne največjo možno vsoto, ki jo lahko izbereš. Pri tem ne smeš
    izbrati dveh sosednjih kovancev.'''
    if len(kovanci) == 0:
        return 0
    if len(kovanci) == 1:
        return kovanci[0]
    vzamemo = kovanci[-1] + nagrada(kovanci[:-2]) #ne vzamemo predzadnjega, ker vzamemo zadnjega
    nevzamemo = nagrada(kovanci[:-1])
    return max(vzamemo, nevzamemo)
# =====================================================================@023290=
# 2. podnaloga
# Za izplačilo nagrade ni dovolj povedati, kakšno vsoto lahko dobiš, ampak s
# katerimi kovanci prideš do te vsote. Sestavi funkcijo `kateri(kovanci)`, ki
# vrne tabelo z izbranimi kovanci, urejeno v naraščajočem vrstnem redu.
# 
#     >>> kateri([5, 6, 4, 8, 1, 2, 1, 1])
#     [1, 2, 6, 8]
# =============================================================================
def kateri(kovanci):
    '''vrne vrednosti kovancev, pri katerih je dosezena optimalna vsota.
    Pri tem ne smemo vzeti sosednjih dveh kovancev'''
    opt_vsota = 0
    for i in range(2 ** len(kovanci)):
        niz = bin(i)[2:]  #stevilo spremenimo v binarno in odrežemo '0b'
        if '11' not in niz:  #preverimo da ne vzamemo dveh zaporednih stevil
            if len(niz) < len(kovanci): #nizu moramo na zacetek dodati ustrezno st. nicel
                niz = (len(kovanci) - len(niz)) * '0' + niz
            seznam_nizov = list(niz)
        vsota = 0
        for i, el in enumerate(seznam_nizov):
            if el == '1':  #pristejemo element, ker je pri vsoti izbran
                vsota += kovanci[i]
        if vsota > opt_vsota:  #ce smo nasli boljso vsoto, obstojeco najboljšo zamenjamo
            opt_vsota = vsota
            max_niz = niz  #zapomnimo si indekse izbranih kovancev
    vrednosti_izbranih_kovancev = []
    for i, el in enumerate(max_niz):
        if el == '1':  #ce je kovanec v resitvi si zapomnimo njegovo vrednost
            vrednosti_izbranih_kovancev += [kovanci[i]]
    vrednosti_izbranih_kovancev = vrednosti_izbranih_kovancev[::-1]
    vrednosti_izbranih_kovancev.sort()
    return vrednosti_izbranih_kovancev
# =====================================================================@023291=
# 3. podnaloga
# Predsednik komisije za nagradno igro pa s funkcijo `kateri` ni najbolj
# zadovoljen, saj mora sedaj, če želi ugotoviti znesek, poklicati
# funkcijo `nagrada` ali pa sešteti rezultat funkcije `kateri`. Zato želi
# funkcijo, ki vrne par - prva je maksimalna vrednost, druga vrednost pa tabela
# kovancev.
# 
# A pozor! Nalogo reši "od začetka", torej pri rešitvi nikakor ne uporabi
# funkciji `nagrada` in `kateri`.
# 
#       >>> naj_vsota([10, 2, 8, 16, 14, 10, 4, 5, 7])
#       (43, [10, 8, 14, 4, 7])
#       >>> naj_vsota([10, 2, 8, 16, 14, 2, 10, 4, 5, 7])
#       (49, [10, 8, 14, 10, 7])
#       >>> naj_vsota([3, 2, 1, 4, 6])
#       (10, [3, 1, 6])
#       >>> naj_vsota([1, 3, 1])
#       (3, [3])
#       >>> naj_vsota([2, 2, 2])
#       (4, [2, 2])
# =============================================================================

# =====================================================================@023292=
# 4. podnaloga
# Blagajnik komisije za nagradno igro pa pravi, da je predsednik malo
# čuden in si z njegovo funkcijo nima kaj pomagati. Želi bolj "vizualen" rezultat.
# Kakšne, je razvidno iz primerov!
# 
#       >>> naj_vsota_kako([10, 2, 8, 16, 14, 10, 4, 5, 7])
#       (43, [10, '_', 8, '_', 14, '_', 4, '_', 7])
#       >>> naj_vsota_kako([10, 2, 8, 16, 14, 2, 10, 4, 5, 7])
#       (49, [10, '_', 8, '_', 14, '_', 10, '_', '_', 7])
#       >>> naj_vsota_kako([3, 2, 1, 4, 6])
#       (10, [3, '_', 1, '_', 6])
#       >>> naj_vsota_kako([1, 3, 1])
#       (3, ['_', 3, '_'])
#       >>> naj_vsota_kako([2, 2, 2])
#       (4, [2, '_', 2])
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
        Check.current_part['token'] = 'eyJwYXJ0IjoyMzI4OSwidXNlciI6MTY2MH0:1ioSSS:TEzjLzj_1ZSkJQ31l10GhLvGA0Q'
        try:
            tests = [('''nagrada([5, 6, 4, 8, 1, 2, 1, 1])''', 17),
                     ('''nagrada([2, 2, 2])''', 4),
                     ('''nagrada([1, 3, 1])''', 3),
                     ('''nagrada([1, 3, 1, 4, 6])''', 9),
                     ('''nagrada([3, 2, 1, 4, 6])''', 10),
                     ('''nagrada([10, 2, 8, 16, 14, 2, 10, 4, 5, 7])''', 49),
                     ('''nagrada([10, 2, 8, 16, 14, 10, 4, 5, 7])''', 43)]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMzI5MCwidXNlciI6MTY2MH0:1ioSSS:LwVSJ1uKRP1OZgPo24aPie0UFlU'
        try:
            tests = [('''kateri([5, 6, 4, 8, 1, 2, 1, 1])''', [1, 2, 6, 8]),
                     ('''kateri([2, 2, 2])''', [2, 2]),
                     ('''kateri([1, 3, 1])''', [3]),
                     ('''kateri([1, 3, 1, 4, 6])''', [3, 6]),
                     ('''kateri([3, 2, 1, 4, 6])''', [1, 3, 6]),
                     ('''kateri([10, 2, 8, 16, 14, 2, 10, 4, 5, 7])''', [7, 8, 10, 10, 14])]
                    # ('''kateri([10, 2, 8, 16, 14, 10, 4, 5, 7])''', [7, 10, 10, 16] ali
                    # [4, 7, 8, 10, 14])]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMzI5MSwidXNlciI6MTY2MH0:1ioSSS:pY8qkrYpve1qVdI9fEsaRA2An70'
        try:
            tests = [('''naj_vsota([5, 6, 4, 8, 1, 2, 1, 1])''', (17, [1, 2, 6, 8])),
                     ('''naj_vsota([2, 2, 2])''', (4, [2, 2])),
                     ('''naj_vsota([1, 3, 1])''', (3, [3])),
                     ('''naj_vsota([1, 3, 1, 4, 6])''', (9, [3, 6])),
                     ('''naj_vsota([3, 2, 1, 4, 6])''', (10, [1, 3, 6])),
                     ('''naj_vsota([10, 2, 8, 16, 14, 2, 10, 4, 5, 7])''', (49, [7, 8, 10, 10, 14]))]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMzI5MiwidXNlciI6MTY2MH0:1ioSSS:IUDLm07_nA4xY8Z1RSWBc-FuGnY'
        try:
            tests = [('''naj_vsota_kako([5, 6, 4, 8, 1, 2, 1, 1])''', (17, ['_', 6, '_', 8, '_', 2, '_', 1])),
                     ('''naj_vsota_kako([2, 2, 2])''', (4, [2, '_', 2])),
                     ('''naj_vsota_kako([1, 3, 1])''', (3, ['_', 3, '_'])),
                     ('''naj_vsota_kako([1, 3, 1, 4, 6])''', (9, ['_', 3, '_', '_', 6])),
                     ('''naj_vsota_kako([3, 2, 1, 4, 6])''', (10, [3, '_', 1, '_', 6])),
                     ('''naj_vsota_kako([10, 2, 8, 16, 14, 2, 10, 4, 5, 7])''', (49, [10, '_', 8, '_', 14, '_', 10, '_', '_', 7]))]
            
            for test in tests:
                if not Check.equal(*test):
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
