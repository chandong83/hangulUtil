# hangulUtil

Python utilities for Hangul



사용방법
==


### 한글 확인


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



### 숫자 문자를 한글로 바꾸기

#### code
<pre>
<code>
import hangulUtil as han


txt = ['1234',
         '190.20',
         '100000.0']

for t in txt:
    print(t)
    print('to')
    print(han.digit2txt(t))

</code>
</pre>


#### output

<pre>
1234
to
천이백삼십사
190.20
to
백구십쩜 이
100000.0
to
십만
</pre>
