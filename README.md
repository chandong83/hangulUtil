# hangulUtil

Python utilities for Hangul



사용방법
==


한글 확인
--


#### code
<pre>
<code>
import hangulUtil as han


txt = ['한글입니다.',
         '한글 pluse English',
         'Just Alphabet']

for t in txt:
    print(t)
    if han.isHangul(t):
      print('it is korean')
    else:
      print('it is not korean')
    print('')
</code>
</pre>

#### output
<pre>
한글입니다.
it is korean

한글pluseEnglish
it is korean

JustAlphabet
it is not korean
</pre>
