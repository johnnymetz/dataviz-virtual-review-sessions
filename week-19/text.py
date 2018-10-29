text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Go GoGo

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

github.com
github*com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Metz
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

The cat in the hat sat on a mat
'''

phrase = "Begin a sentence and bring it to an end"

emails = '''
JeffPBezos@gmail.com
jeff.bezos@ucsd.edu
jeff-321-bezos@amazon-work.net
'''

urls = '''
https://www.google.com
http://jeffbezos.com
https://youtube.com
https://www.nasa.gov
'''
