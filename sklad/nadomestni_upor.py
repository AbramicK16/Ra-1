# =============================================================================
# Nadomestni upor
#
# Kot je dobro znano iz elektrotehnike, nadomestni upor dveh zaporedno
# vezanih upornikov izračunamo po formuli $R = R_1 + R_2$, nadomestni
# upor dveh vzporedno vezanih upornikov pa je $1/R = 1/R_1 + 1/R_2$.
# =====================================================================@021977=
# 1. podnaloga
# Napišite funkcijo `nadomestni_upor(r1, r2, tipV)`, ki kot argumenta dobi
# dve števili `r1` in `r2` (tj. upor obeh upornikov) in tip vezave `tipV`,
# ki je bodisi znak `'V'` bodisi znak `'Z'`. Funkcija naj vrne nadomestni
# upor vezja.
# Pozor: nekateri uporniki so vezani kratkostično in imajo upor 0.
# (Upor dveh vzporedno vezanih upornikov, od katerih ima vsaj en upor 0, je 0.)
# 
#     >>> nadomestni_upor(3, 5, 'Z')
#     8
#     >>> nadomestni_upor(3, 0, 'V')
#     0
#     >>> nadomestni_upor(2, 5, 'V')
#     1.875
# =============================================================================
from sklad import Sklad

def nadomestni_upor(r1, r2, tipV):
    '''Vrne nadomestni upor vezja. Argumenta sta dve stevili r1 in r2
    ter tip vezave, ki je bodisi znak 'V' ali 'Z' '''
    sklad = Sklad()
    if tipV == 'Z':
        return r1 + r2
    if tipV == 'V':
        if 0 in (r1, r2):
            return 0
        return (r1 * r2) / (r1 + r2)

# =====================================================================@021978=
# 2. podnaloga
# Sestavite funkcijo `upor_vezja(niz)`, ki izračuna nadomestni upor vezja.
# Vezje je podano kot niz v "RPN notaciji": operandom (tj. vrednosti uporov)
# sledi operator (tj. način vezave, `'V'` ali `'Z'`).
# 
# Analizirajmo vezje `'3 5 Z 0 V 3 2 Z V'`: 
# Niz `'3 5 Z'` tako pomeni, da sta zaporedno vezana upornika z upornostma
# 3 in 5 (ki ju lahko nadomestimo z enim upornikom z upornostjo 8). Skratka,
# dobimo vezje `'8 0 V 3 2 Z V'`.
# V tem novem vezju niz `'8 0 V'` pomeni, da sta vzporedno vezana upornika z
# upornostma 8 in 0. Vzporedna vezava, ki vsebuje kratkostični upornik, je
# kratkostična, zato je 0 nadomestni upor vezja `'8 0 V'`. Skratka, dobimo
# vezje `'0 3 2 Z V'`.
# Niz `'3 2 Z'` pomeni, da sta zaporedno vezana upornika z upornostma 3 in 2
# (in torej z nadomestno upornostjo 5). Če upoštevamo še to, potem dobimo
# vezje `'0 5 V'`, kar na koncu da rezultat 0.
# 
#     >>> upor_vezja('3 5 Z 0 V 3 2 Z V')
#     0
# 
# Predpostavite lahko, da v nizu `niz` nastopajo (poleg znakov `'V'`, `'Z'`
# in `' '`) le nenegativna cela števila.
# =============================================================================
from sklad import Sklad

def upor_vezja(niz):
    '''Izracuna nadomestni upor vezja. Vezje je podano kot niz v
    "RPN" notaciji'''
    skladUporov = Sklad()
    for znak in niz.split(' '):
        if znak in 'ZV':
            prvi_el = skladUporov.vrh()
            skladUporov.odstrani()
            drugi_el = skladUporov.vrh()
            skladUporov.odstrani()
            skladUporov.vstavi(nadomestni_upor(prvi_el, drugi_el, znak))
        else:
            skladUporov.vstavi(int(znak))
    return skladUporov.vrh()

# =====================================================================@021979=
# 3. podnaloga
# Napišite še funkcijo `sestavi_racun(niz)`, ki namesto da izračuna
# nadomestni upor vezja, sestavi račun, ki ga je potrebno izračunati,
# da dobimo nadomestni upor vezja.
# 
#     >>> sestavi_racun('3 5 Z 0 V 3 2 Z V')
#     '(1/(1/(3 + 5) + 1/0)^-1 + 1/(3 + 2))^-1'
# 
# _Namig_: Ali lahko nalogo rešite tako, da malenkost predelate rešitev
# prejšnje naloge?
# =============================================================================
from sklad import Sklad

def sestavi_racun(niz):
    '''sestavi racun, ki ga je potrebno izracunati, da dobimo nadomestni upor
    vezja'''
    skladUporov = Sklad()
    for znak in niz.split(' '):
        if znak in 'ZV':
            prvi_el = skladUporov.vrh()
            skladUporov.odstrani()
            drugi_el = skladUporov.vrh()
            skladUporov.odstrani()
            if znak == 'Z':
                skladUporov.vstavi('({0} + {1})'.format(drugi_el, prvi_el))
            else:
                skladUporov.vstavi('(1/{0} + 1/{1})^-1'.format(drugi_el, prvi_el))
        else:
            skladUporov.vstavi(znak)
    return skladUporov.vrh()


# =====================================================================@021980=
# 4. podnaloga
# Stari električarski mački si račun poenostavijo na sledeč način: če je
# upor $R_a$ več kot 10-krat večji kot upor $R_b$, potem za nadomestni
# upor zaporedne vezave upornikov $R_a$ in $R_b$ vzamejo kar $R_a$, kot
# nadomestni upor vzporedne vezave pa kar upor $R_b$. Seveda pa pravilno
# razumejo vezavo, če je kakšen upor enak 0.
# 
# Sestavite funkcijo `stari_macki(niz)`, ki bo nadomestni upor vezja
# izračunala po "metodi starih mačkov".
# 
#     >>> stari_macki('2 30 Z 20 V 3 2 Z V')
#     3.5294117647058822
# =============================================================================
def nadomestni_upor_SM(r1, r2, tipV):
    '''vrne nadomestni upor po principu stari macki, pri ceme sta
    r1 in r2 upora, tipV pa tip vezja'''
    if r1 * r2 == 0:
        return 0
    if 0 in (r1, r2):
        return 0
    if r2 > 10*r1:
        return r2
    if r1 > 10*r2:
        return r1
    if tipV == 'Z':
        return (r1 + r2)
    if tipV == 'V':
        return (r1 * r2) / (r1 + r2)

def stari_macki(niz):
    '''nadomestni upor vezja izracuna po metodi stari macki'''
    sklad = Sklad()
    for znak in niz.split(' '):
        if znak in 'ZV':
            prvi_el = sklad.vrh()
            sklad.odstrani()
            drugi_el = sklad.vrh()
            sklad.odstrani()
            sklad.vstavi(nadomestni_upor_SM(prvi_el, drugi_el, znak))
        else:
            sklad.vstavi(int(znak))
    return sklad.vrh()





































































































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
        Check.current_part = None
        Check.part_counter = None

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
        Check.current_part['token'] = 'eyJ1c2VyIjoxNjYwLCJwYXJ0IjoyMTk3N30:1iIZiA:dXWAN6dqoilWebo5duomPiBtPEI'
        try:
            test_data = [
                ("nadomestni_upor(3, 5, 'Z')", 8),
                ("nadomestni_upor(0, 0, 'Z')", 0),
                ("nadomestni_upor(3, 0, 'V')", 0),
                ("nadomestni_upor(0, 0, 'V')", 0),
                ("nadomestni_upor(0, 3, 'V')", 0),
                ("nadomestni_upor(3, 5, 'V')", 1.875),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
            Check.secret(nadomestni_upor(4,7,'Z'))
            Check.secret(nadomestni_upor(4,8,'V'))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoxNjYwLCJwYXJ0IjoyMTk3OH0:1iIZiA:_snO4Wtz06DQZ-YBXePhE8vUDsg'
        try:
            test_data = [
                ("upor_vezja('3 5 Z')", 8),
                ("upor_vezja('3 5 Z 0 V')", 0),
                ("upor_vezja('3 2 Z')", 5),
                ("upor_vezja('3 5 Z 0 V 3 2 Z V')", 0),
                ("upor_vezja('2 30 Z 20 V 3 2 Z V')", 3.555555555555555),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
            
            Check.secret(upor_vezja('3 4 Z 2 1 Z 5 Z V 3 2 V 3 V 1 Z V'))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoxNjYwLCJwYXJ0IjoyMTk3OX0:1iIZiA:VByLEtr_DtZj98OUQ6LB-OcZlbI'
        try:
            test_data = [
                ("sestavi_racun('3 5 Z')", '(3 + 5)'),
                ("sestavi_racun('3 5 Z 0 V')", '(1/(3 + 5) + 1/0)^-1'),
                ("sestavi_racun('3 2 Z')", '(3 + 2)'),
                ("sestavi_racun('3 5 Z 0 V 3 2 Z V')", '(1/(1/(3 + 5) + 1/0)^-1 + 1/(3 + 2))^-1'),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
            
            Check.secret(sestavi_racun('3 4 Z 2 3 Z 5 Z V 5 2 V 3 Z 1 Z V'))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoxNjYwLCJwYXJ0IjoyMTk4MH0:1iIZiA:4PGgWhyttSux15ahWWZa3xesDZ8'
        try:
            test_data = [
                ("stari_macki('3 5 Z')", 8),
                ("stari_macki('3 5 Z 0 V')", 0),
                ("stari_macki('3 2 Z')", 5),
                ("stari_macki('3 5 Z 0 V 3 2 Z V')", 0),
                ("stari_macki('2 30 Z 20 V 3 2 Z V')", 3.5294117647058822),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
            
            Check.secret(upor_vezja('3 40 Z 2 1 Z 5 Z V 3 15 V 200 V 13 Z V'))
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
