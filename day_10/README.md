# Día 10: Combinatoria

Hemos podido interceptar varios textos,entre ellos una localización, pero las letras de algunas palabras están mezcladas. Deberás generar un código que genere todas las posibles palabras de las letras dadas:

- AITLAI
- AMOR
- NOITCAAV

Las reglas de la gramática son:

- Usar todas las letras en cada combinación
- Generar todas las posibles palabras aunque estas no sigan las reglas de la gramática.
- El ingreso puede ser por consola o con los datos quemados en el código.

- [Día 10: Combinatoria](#día-10-combinatoria)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Contexto

Para este reto debemos permutar los caracteres proporcionados, para ello podemos usar la función `permutations` del módulo `itertools` de Python. Usaremos permutaciones en vez de combinaciones debido a la regla de la gramática que dice que debemos usar todas las letras en cada combinación.

## Solución

Importamos el módulo `itertools`.

```python
from itertools import permutations
```

Definimos una función que recibe una lista de caracteres y retorna una lista única de palabras (de ahí el uso de `set`).

```python
def gen_words(chars: str) -> list:
    words = ["".join(x) for x in permutations(chars, len(chars))]
    return set(words)
```

## Ejecución

Para ejecutar el programa debemos ejecutar el siguiente comando:

```bash
python .\main.py <chars>
```

## Resultados

Caso AITLAI ([salida](output/AITLAI.txt))

```bash
python .\main.py AMOR

{'AMOR', 'AMRO', 'AOMR', 'AORM', 'ARMO', 'AROM', 'MAOR', 'MARO', 'MOAR', 'MORA',
 'MRAO', 'MROA', 'OAMR', 'OARM', 'OMAR', 'OMRA', 'ORAM', 'ORMA', 'RAMO', 'RAOM',
 'RMAO', 'RMOA', 'ROAM', 'ROMA'}
Generated 24 words
```

Caso AMOR ([salida](output/AMOR.txt))

```bash
python .\main.py AITLAI

{'AAIILT', 'AAIITL', 'AAILIT', 'AAILTI', 'AAITIL', 'AAITLI', 'AALIIT', 'AALITI',
 'AALTII', 'AATIIL', 'AATILI', 'AATLII', 'AIAILT', 'AIAITL', 'AIALIT', 'AIALTI',
 'AIATIL', 'AIATLI', 'AIIALT', 'AIIATL', 'AIILAT', 'AIILTA', 'AIITAL', 'AIITLA',
 'AILAIT', 'AILATI', 'AILIAT', 'AILITA', 'AILTAI', 'AILTIA', 'AITAIL', 'AITALI',
 'AITIAL', 'AITILA', 'AITLAI', 'AITLIA', 'ALAIIT', 'ALAITI', 'ALATII', 'ALIAIT',
 'ALIATI', 'ALIIAT', 'ALIITA', 'ALITAI', 'ALITIA', 'ALTAII', 'ALTIAI', 'ALTIIA',
 'ATAIIL', 'ATAILI', 'ATALII', 'ATIAIL', 'ATIALI', 'ATIIAL', 'ATIILA', 'ATILAI',
 'ATILIA', 'ATLAII', 'ATLIAI', 'ATLIIA', 'IAAILT', 'IAAITL', 'IAALIT', 'IAALTI',
 'IAATIL', 'IAATLI', 'IAIALT', 'IAIATL', 'IAILAT', 'IAILTA', 'IAITAL', 'IAITLA',
 'IALAIT', 'IALATI', 'IALIAT', 'IALITA', 'IALTAI', 'IALTIA', 'IATAIL', 'IATALI',
 'IATIAL', 'IATILA', 'IATLAI', 'IATLIA', 'IIAALT', 'IIAATL', 'IIALAT', 'IIALTA',
 'IIATAL', 'IIATLA', 'IILAAT', 'IILATA', 'IILTAA', 'IITAAL', 'IITALA', 'IITLAA',
 'ILAAIT', 'ILAATI', 'ILAIAT', 'ILAITA', 'ILATAI', 'ILATIA', 'ILIAAT', 'ILIATA',
 'ILITAA', 'ILTAAI', 'ILTAIA', 'ILTIAA', 'ITAAIL', 'ITAALI', 'ITAIAL', 'ITAILA',
 'ITALAI', 'ITALIA', 'ITIAAL', 'ITIALA', 'ITILAA', 'ITLAAI', 'ITLAIA', 'ITLIAA',
 'LAAIIT', 'LAAITI', 'LAATII', 'LAIAIT', 'LAIATI', 'LAIIAT', 'LAIITA', 'LAITAI',
 'LAITIA', 'LATAII', 'LATIAI', 'LATIIA', 'LIAAIT', 'LIAATI', 'LIAIAT', 'LIAITA',
 'LIATAI', 'LIATIA', 'LIIAAT', 'LIIATA', 'LIITAA', 'LITAAI', 'LITAIA', 'LITIAA',
 'LTAAII', 'LTAIAI', 'LTAIIA', 'LTIAAI', 'LTIAIA', 'LTIIAA', 'TAAIIL', 'TAAILI',
 'TAALII', 'TAIAIL', 'TAIALI', 'TAIIAL', 'TAIILA', 'TAILAI', 'TAILIA', 'TALAII',
 'TALIAI', 'TALIIA', 'TIAAIL', 'TIAALI', 'TIAIAL', 'TIAILA', 'TIALAI', 'TIALIA',
 'TIIAAL', 'TIIALA', 'TIILAA', 'TILAAI', 'TILAIA', 'TILIAA', 'TLAAII', 'TLAIAI',
 'TLAIIA', 'TLIAAI', 'TLIAIA', 'TLIIAA'}
Generated 180 words
```

Caso NOITCAAV: La dalida de este caso se encuentra ([aquí](output/NOITCAAV.txt)) dado que la cantidad de palabras generadas es muy grande.