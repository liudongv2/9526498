"""
cookies格式 ppxck = "cookie#xa#xl#url#ua#备注"
url 为 ？号以后部分
"""
bfs = 10  #并发数

# 钱够就提 , 1是开启 , 否则就10元提现
is_mini= 1
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(bz2.decompress(b'BZh91AY&SY V8N\x00\x03>\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\n\x9f)w={\xef\x9eg}\xf1n\xf7}\xf6\xb7\xd6\xeeL\xed\xee\xaa}\xea\xee\xfb\xba\xbe\xdeL\xf9w\xb6\xe6\xdeBO\t\xa9\xb2=\x1ah\x99\xa56&\x83\x1a\x9aa\'\xe5=\'\xa9\xea\t\xfa\x93\x13d\xd0\x19\x94z\x9a\x1a\x9f\xa9<\x9az\x8dO\xd4b=\r\x082\x9e\xa7\x89\xe8\x9a\x9e\x83G\x911\x1e\x93O(\xf5=M\x1e\xa6\x9e\xa1\x89\xa6\x98\x93\xd4y26\xa6\xd2zhi\xeaa\x0c\x8c\x8c\x98F$%<\'\x93T\xd9G\xa9\xe0\x1a\xa7\x99\x14\xc3\x13)\x99\x1a\r4z\x9b$\xf5\x10y\'\xa6\x08\xdaB~MM2z\xa7\xe9\xa9\x88\xda\x05<\x98L\x93\xdaS\xd3h\x00I\xe1G\x83$\xf41\x1a\x1a\x9e\x9944\xd0\xcai\xb1\x03RxM2256\xd2zL\xd0L\xd5\x10\x8fSi4z\x9eP\x0fS\x1a\x9bPd\xc6\x84m\x13&\x98M\xa8\x0c\xd4\xdaF\xd0j\x19\xa4z&\x9e\xa6&&@\xc2\r\x90\x19G\xa6\x93\xcazi\xa1\x92zdjm d\xc8i\x84\xc9\xe4\x86e\x0f@L\xd2mOH\r6\xa7\xa9\xa3\x13\'\xea\x8d4\x08L\x99\x19\xeaLCOBz\x9az\x04\xcd2\x13OQ\xeab\x19\xa9\xa3\x11\xa6\x98\x81\x93hOS\x06\x8c\xa6\xd4\xf5=M\x81\x0c\x8d4\x08\xd0\xfdI\x80OS\xd4\xc9\xa6F\x86\x8d\xa14\xd3&F\x990\xd4b4\x0fi2\x8fHz\x992\r\x18C&\x86D#e\x1adzOD\xd9\x13\xc50\x9bSF&i\x1e\x93h\x9e\xa7\x9a\x83\x11\xa1\xa9\xfa\xa6\xc2A\xeai\xa1\xe9\xa8\xf52=A\xa6\x8fQ\xea`\x10i\xead\x1a4\xd3h\x02\x06M6P\x1a\x07\xa4<\x90y&G\xb5&\xd4\xc8\xf5\r=&\x9e\xa3\x10i\xa1\xa3M2\x192\xa7\x93\x13G\xa4\xd3\x12zh\xcaa\xeaM=&\x9a\x0f$\xd0\xc9\x88i\xb4\t\x8dLe\x18M6\xa7\xa0\x994\xc4i\xe9\xa42i\xa3\xd14\xc8i\xa6\x8d\xa84\x0fD\xc8\xd1\x886\xa0hi\x8dFC\x11\xa3\x13ji\xa7\xa2d4\xda\x1a\x8d\x06\x86@, \x91\x02(p\xb0\x9e\x97\xc6\xea\x0b\xe7\xcf\x8c\x1b\n\x08\xa0\x00j\x04Qkp\xa3\xc1\x00\xd5\x01\x14\xf2p\xbaTC\x85I\x15\x08\x89X\xe0\x05"\xa8\x18\x00\x12)\x82\x83\x90c\x97\x16\x06\x90\x13\xf7a0\x9f#\xbfL\xe9|M\x88\xa8@\n\r\x03&\x14\xc1"\x82\xec\x18i\xe1\x92b\x14P\xff(\xcat\x8d\xc6M8P\xb3=\x19\x1d0\x80x\xef\xea{c\xf2\xb8\xf6\x88\x008\xe8\x90%\xfd\xd8l>e\xd3\xc9\xddB\xefd\x19\x8a\xc1\\5\x88d\x16\xb6"\x95oc,\xc6\x02pD\x04\x9b\x9a\xc1\xc0I\xbe\xba)\xaa_k\ry\x95\xb6\xa2\xe0\xbc\x86@\x8d\x91\x9e\xecl\x12wO*zH\x9f{\xb0\x91KRM\xe0\xd1\x95\xbfkE\x04\xcdf\x16\xcd\xc6\xcba\xedx\x9f\x1e\xba\x08\xf8rS\xaa\xa5\x16\x1e\xe7;2a\xa5d\x1e\x95\xca\xbc\xec\x03\xad\xa9\xa0+\xffvuk\x12\xd8d\xf8/\x15>\xee\xaa\x12\xef;\xaa\xccY\x03b\x9f\xa9\x85\x98\xe8G\xa6\x9e\xc2\xd7\x1c\x97\x1e\x80!J\xa6\xf7\xcb\x15\x07\xaf\x87N\x13\xde\xd1w&\x89Q\x8f\xd2\x9b\xb6\x0c\x11\xb5\x11\xc7\xc9\x90\x08Eoa\x95\xfb\xc3G\xd6pg\xeaY\x9b\xd9\x08\xff\r,!z\xbev]\x82\xc7\x10X\x02\xdd\xdb\xd7\x18}Rn\xde\xdb\x93\x80Q\x83\xe3\xf2\t\xbc\xc3<*\xa4B\xad\xccp\x10\x8f\xc2\xff\x015\x03\xe1\n\xb5A\xaa\xc5\x0eK?\xc1\xcf\x8d\xaa\xba*c\xb5\x9b\xc0\xda\xfb\x0c\x89\x8b3\xde\xb5\x02\xbe1\xb9L\x8dbK\xccVk\xf5g\x08{=\xa6\xa9`Y\x9f\xed\xfd\x17g5\xfa~I\xf8\xc6\x02\x1c\x89\xa1N\xfe\xdaO\xa6\xdf\xa1\xe5O6~\x95m|i6*mu\xb1\xa0\xf1\xfe\x89\xb2tf\n\xa0q\xe7|\xc8nR\xb6d\xac\xd6pLv\xe2\xaafr\xc6x\xf3?\xa5\x07\x89]\xa7\xc8\xcc\xdd\x82\x15!\x87\xb5\xab\x15?uT\xefFY\n\xec\xfb\xb0i\xed\xec\x0c\xa3\x9e_\x84\x99\xa3\x9b\xb9\xf27\xe5?\x9b\x98A\xbfV\x9b\xcb\xa2w\x82\x86d\xf8\x8d\x80\xcc\x18x=E\xdf\xd2g\xfcu\'+\x8c-\x8di\x8d\xd7u\xc6?=\xf7\x97\xd5\x95\xfc\xedLW\xd0O"\\\'q\xaf\xea\xa6\xc2\xc8-m\x01\x926\rY\x9c\xbev\xb1\xea\x95\n\x06\x88(Ob\xd6\x89\xb5\x8a<=\xde\x94\xef\xdc\xe8\x01\x8a\x16#\x01&\xd6t\x90\xfb\xfb3+>S\xd7\x00S\xb6\xc1\xdd\xb0\xa7Jc5Z\xcb\x08\xe9\xf5=3g\xff79\xbd\x86z\xb1Q\t\x03q#\xe8\xd2\xdd\x12$\x81\xc7#\xa8\x89x\x87HU\x9f\x14\xcb\xb7\xad\xf8N\xdf*7\xb1\xa5\xef\xd8k\xdc\x82\xd6\xb3\xf6\xcc0\x7f\xb4}\xd1\xb2\xe7d\x90\x00\xd3i\x82\xebO\xf0\t\xd3&\xd3\xc4\xd5\xdd\xfd\xabc\x1fk\xb6,mf\x1c+(\xa5\xa6\x06;\xd2\x8f\x9a\x11\x1e\xa8\x0fnm5\xba\xaf[\x93aDOS\xce\x08`\xbb\xdb|\x04\xcc\x80ON\xab\xc1\xc6\xbb\xdb\xe7\x8be\xd1\x1e\xcd=C]Ph\xcb\x8c\xd0\xd7\xc9\x8b\xdd\xd1\xcb\x10\x18\xe0ZR\xe1\xdf\r\x7f\xe3\x85\xf1\xf3m\x07&\xa5PI\x13\xc9\x89\xafQ\xb2*\xd8\xa5\xde\xe5$\x8d\x16\\\x17+!\xf8\x10!\xce)q\x9c\xb4\x9a\xfd\xa3B\x9a\xfc\xd6\xe0\x9cB\xe0HU.\xf3c%\xc1\x860\xba(\x05\xae\xc2\x9c\xfc\x9aG\xc9y\xb7\x04w3\xa2\x94\x97\x1dJt\xca\n9\x83\xe0\xaf\x0bvQ\xd7mN8\x85_l\x1a\xd82\x02\x10\xc8\xf3\xfbE\xdf\xc7\x92E\xb0\xa1\x9b\xf5\xb9bl\xea\xf8a*<\xac\xdf\xeb\x986i"\xd6vQ\x07\x1a\xaf\xc8\x83\xae\x89f\xadC\xc5\xb7f\x84\x90m\xdf\xcf\xd5\x1di\xcbs{\xb5\xc9\x88\xa5\x11|\xccw\'4|\xbcVX\x99\x1f\x1b\x9b@\xf3\xe7\x18\x10\xde\xdaY\x00.\xd5\xf2Po\xfbA\x91\xd8K\x95\xcf\x1f\xee\xc2\xd6)\x1b\x17\x85]\xf1pz\x13\x8as\x84\x8dD 9\xc9\x86\x99\xe4\x9d\x90V/\xffq\xc2\xdc\xa5\x91ER\xacF\xea\xe2\xc7\xabG\xf0\xc93\xce`\x0bI\xa9\x04+\xac\x83\x8eeF\x12\xf6\x1bkk\xb4\x9b\xbd\x0b\xe0\x10N\x96\x90\xfd\xca\r?F1g\x130\xc3\xb1:J\x1e\xae\xf1\x90lKe\xe6\x92\xde\xacE\x87\xd3\xd9E\x01pJ\x9e\xfb\xde+\xf5E\xb1\xbd\\\x18\'~i\x07Y~7F0\xbc\xad@\x1e\x8bH\x88\xf5I}N\xae-h\x00%/\x19\x8f\x16\xd6i\xf3\xfcl\x92\xa2\x82*\xddN1\xa4\x1f,xk\x92X\x97\x17\xd2\x0cf:\xf0\xd5F4,\x12y"\xddd\xa3\x9e\x0e\x1cXwY\xe7\xbcvy\x8a-\xbdt\x90\xc4\xd6$\xbd9\xf5\x85f\x07&\xb8\xeb\xd9\x1b\xa8C\xa1\x1e\n\xca\xcaTc\x16\xcaRU\xd1\x8c}\xb6O\xba!\x97\xcb\r\xaf\x99\xcf\xcc?\xa0\xed\xb1s\x0b$i\x96\xa9#\x8f\x7f9.\xeb*o\xde\xeeeux\xdfo-\x8a\xfci\xc4\xc5\xcc|\x8d&\xca2\xee~ OX\xff4\x92b\x1d\x18L\xcf\x82\x06\xf3\x13\xc3\xe4"<Yxhx\x1aC@\xd7\x05o\xefK8\xbc)\x02\xae\x96\x8a\x979+\x0c\x1fO\xc7#_\x80\rdsNl\xd3*\xec\x9e\xafS\x189\xc3"\xc2\xe6=\xd9\x9cGb\x1eB\x95\x08{\\l4\xe8\xce\x1a\x98c\xd5\xe5)j\x84\xb2`\xc8;\x16\x97\xa6u\xc1-T\xb9+\x1e4\x90(\xa2*q\x03\x13\xa28\x06p\xcb\x07=?\x9c;v\x8c!\xb5m\x80\x1e\xc5\xd8\x85\xa6cA\xf9E\x8b\x1c\xe4\xe6R\xfe%x\x8b\x8d\x14w\xb2\x84t\xed*~\xddU\xcb!@\xbc\xbbBTA\xe3bD\xb6y]\xcd\xa9N\x18\xc9\x00\x84\x16\xbeg{\xa6)A\x83\xbdL\xddL\xc9\x99\xa9a\xe9\xaf\x1c_\xb6\xfb|H\xd7\x8a\x1dm{W\xf2\x00\xec\x15a\x12\'\x88n\x9b\x9dM\xe6bH\xcb\xab\x17\x81\xa6\xd6igb(e2\xd5;\xc6D*\x80\xb5\x01k\xf3)\xcf\x064n#1\xa2N6\x1d%\xf4\xb1\x1d\xa7\xb0l\xa9\x11\xad\xb7\x7f\xf2\x97`-\xaa\xce\xe542&B*\xd3\xc8\xb0\xfe\x04\x8b\x87\xc2s\x90\x95@\x9a\x9e\xb1>\'}\xde\x02#k\xda\xc2\xa6k\x1b(au\xeafI\\\x8aH\xe3.\x1f\x89]\x8c\xe0\xa7\xf5\x10\x94\x99\x17\xf1/3\'\xc3\x86\x9eO\xc3\x04\xc3\xcd\xc37\x93L\xa6\x00\xdb\xa4e\xd8\x9b\xd4n\xd5>\x0e\xe2\xb478\x1f\x16\x96{l\xe7=\x0c\x02\xecic\x13V\x0e\x8dEJ\xbc\x95m\xd0h\x1e\xddy\x1b\xa21\x17\xf0\xc0v\x8c\xfb\xd8\xce\x14\xab\xaf\xcba\xc1\xef\xc4T\xae\xa9.\xb6\x05Ry\xd4\xf6\xc6\xf0S\xc3\xfatj\xaclFG\x88@\x18\x02!\xa1P|\xe43\xca\x02\xf5\xa1\xeaDIz\xf4\x1d\xd2\x15\xdaJ\xbc\x0f?5\xc3g:\xadn s\xfb\xb4\xe9\xb1\xf8S\xe1\xdb\x9e\x85\xa4o\xf8W\x8an@g\x17\xbd\xa8\x84\xf0\xb8J\xbdW\x11\xa5\xf2#\xea\xe9Ut\xf6W<\xf9|\xa8\xd4\x95\xa02\x9dF\x1er\xbc\xc1\x94}*;y\xf4*\x88\xfe\x1b\xf6\xc6\x87\x87J1\xb7PK\xf2S\xeb\xc5\x16\x8f\xdf\x96\xd4 \xc2\x12\'\xa9f\xaa&4\x88_(t\x9f\xedJ\xd3C\x14\xeeH\xbe\x07~\x88\x0f\xd8\xf0d=I\xe8_\xe8 O\x8dbBD\xf1\xc3\x16\xb0\x8be<E\x15h\xa3+kI\xc7<"i\xc2A>DE\xa861\x02\x10GA\xfd`Q\xf6\xcf\x07\x95\x0f\xc9\xcd\t2\x84\x08\x93\xbd7\xf3\xb5\xb3T\xdb\xe3\x87\xa9\x97\x8e\xb94\xd1\x0b$\x1c%\x0cu\x8a\x14\x9a\xb2\xed\n\xe5\xa8_\x07&\x93\x9e)\x10\xae\xed\x8b\x0fr\x9e\x97z\xed\x98\x83l2\xdf28 \xdb\xe6\x9b\xaf<\xaa]\xf6\xea\xf3\x94\xe6l\xb1\xb05W,-s\x9bg:!8j\xff\x9b\xbd\xdf\xaad-\xe6\xf3Qt\xfa\xf5\xd6CLsm\x83S\xd83\x0e\x04\xa7^w\xae\xd0\x8c\xca\xdfh\xd3|6\xd1/hXO\x1d!g\xf2\x8a\x19\xf2\xa4TW\xab\x05F\xee\xae\xb9\xc7\x19\x92q\xf4E\x01p\xa2\xa2l96Wy\x16U\x03\x0b\x03\x93\x00\xc5\x1a\x85X\xb4\xfb\x086\x93 \xb4\xfe\x88?\xac)\x01\xfc\x9e\xc0\xe6kH\x8d\xda,\x1b\x01\x16\xe2\xe4H\xd9\xd8\xa6mG\x1bF\x04\x02\xc6\xe5\x1e\x15\xacO3\xbd\xbe\xea\x1cg\xdc\xcbX\xa6\xab,+H\xa5\xcd|\xbe\x8e\xc2\x9c\x17T1\x06\xfa\x04\xc1\xae\xe7\xd1\xdaA\xdf\x9bK\xeb\xae\x82{/j\xd8Q\x06C\x9c\x96\xde?N\xab\xd6\xf2+i-\x89e\xa5\xd7G1\xb9\xba\xbb\xd1\xa0\x8f\xcef\xd0\x95e*\x08\xdb\x98\xc6\x82w\xd0=\x08X\xb7)%[g\xf0O\x12n\xd9\x17%\xa3\x9dX\xbf\xa3\xc5\x8f\x076\xe0\xcb8\xf7\xbe~\xbd\xa2\x00\xcbo\xe3:M\xc1\xe5\xee\x02k\xcd\xebACM\xcb\xb5\xe0\xebl\x8a\xa6\x83_\xc4\x87|A\xbdu%v\xe8"\xae\x8e\xfd\'\xe3\xa4t\x18\x05c\x06C\xd7)7s4\xfd\xa7\x91>\xfa\xec+\xed\x1f\xedk(\xea.\xd1\xff\xf2|\x0cY\x86dg\xbbI\x0b\xe5\xc7*\x11\x1cn\xc8j\xbd#\xb8P\xc7\x97\xfa\x94\x8b\xdc-\x9b-^lP\xef\x11\xb4F\x12DB\xb6\xc3UU\x7fB\xe2\xb9"\x8e\xcbK\x82r\xbdq\xae\xc3\xec\xc7\xb8{\xbd9\xb3\x15\x9f\x0cw=\x13\xd5\xdem\x9c[{\xff\xf5M\xe4\xfc\x13xKFYU\xa4R C?\x8e\xc9$\xe5\x00\x8b\xd3T\x03\xc2GW\xf7;\xe2\xd5\x01\xc7X\n\x08\xe8\xf6\xd1\xccc\xc0!\xf5\x8b\r\x92\xb9fO\xb0e\x18:\x96|\x19\x1e\xd7U\xee\x0b%s\\\x03\x04\x83\xff.\xe1\x0c\x95K\xcf\x1f\xef\xe3\x02\xf3\xa4\xa7\xe1v\xc8\xe9\xed\xcb\x88\rg6\x9b\xbb\xf2bZ\x19\xb1|\x1dZ(\xc9q,-|\x0c\x16e\x82\xb1BaH\xd0`S1\\\x15\x08\xed\x0c\x9b\xc8\xb4\xe7\xd0F\xdf\xcb\xd6\xb7C\xd6Z^\x9a\xb7I8\x1ar\xe5\xaacK\x8c[\xfd]E*\x04\x1f&\xf4\x0ft4\xed\x8e\xeb\x96|\xe49mj\xd8\xeb\x8eQ\x1a\xfa\xeb\xce\xdb\xe6\x05\xe8y\xd9\xb4\xfcS\xa7\x9e\x8c.5\x11\x1d\xb7\xa1r\x8e\xf9\x87\xdd9\x93-.\xca\xedY\x9dj\xc7\xbf\xbc]\xd7j\x1fl^\x0c\xbe~\xb1NpL\x95Y\x96\xb4\x93\xc5\x83\xb4Mzp\x05A\x9e\x84\x8b\x08\x8fDN+;\xeb\xf1\xb4\xd4\'9M\xa8\x1f\x8b4\xc9?\x9fMi\x1c&\x19\xae&{ \xa9\xe9\xbd\x12\xb1e)TL\xc8\xbb\xe1\xa1\xbcb\xbe\x82\xb2\xaaU/\xe1\xb8\x92\x12q+I`pN"\xc1\xbb\x8e\xd2\x0e\x87<\'\x1b\xebt\x86z\x90m\xf4(\\\x81\xe4O\xac&\xf4\xa2\xa1\xa5]\x07\xaa\xa7\xd0\x17\xf2\xb0\x9f\x1cD\x1fJ\x03\x8c\xb1\xf7p.W\x15\x14A\n\xc2\x8c4\x9e)\xbc`\xdeFe\xb1NT\x1d\xe6\xe6g\xbf-1jO\xa9t\x80\x1b6oUY\xfc\x16\x8d\\\xd8\xf6\xbf\x9c\x9d\xbc\xa0\x0f\x0b\xd1\xfb\xaa\x89\xde\xb5\xd2fA\x11\xec^\xe8\xe0\xa4\xe1\xe5.\xdaE\xd9\xe5\\#YP@?X\xea\xc4\x1c\xf4\xf4B\x9em\xb1\xb6\xd6\xb9\xf8\xc4q)\xe1\x1d\xdb\xe0\xf6p8=\xd0\x96\xc3\x82@\xf7\xc2B\x18\xa9\xc7\xe2Xc<\x90n\xaf\xa8s\xae\xbc\xa4\xcd\xd6\x8a\x1fA\x84\x9e\xda\x94\xf8\x8e\xba%\xbb@\x10\xef*\xe6\xce\x02p\xb2\xb2l\x9c\xba\x89\x99\x0fB.\x01\x91\xcb}\xa2\xdeDrw\xea\xddd\x84P\xd0X\xa0\xf5\x03*\xa0A\xd5)\xee\x94\xd8VpLA\x10{j,\xc4\xf0\xeeR,\xd2\xc7J\xea\xafS\x80\xb4g\t\xb3\xf4>\x99G\x9bbUn\xa8\xad\x11\xdf_\xe3\xd5M\xae4\xd4\xb3\xb3\x1e\x9dTi[\xf4\xe9\xae\x84\x1a\xe2\xfb\xbcTQ\x1dv\xd3\xd4\x04\xa7\xe47\xe8\x8e\xb1Cqpn0o\xe3\xd28\x84ew\x9dL\x02\xd348y \x15\xf5\xe2%\xbaQ\x08\x0e\xf0\xc9\xe7\xb8\x89\xcb\xc6\x1a"ee\xa5\xa1\xe3\x15\x85\xd9\xd8\xda\xa3x\xcai\xf9:;W\xc0B\x9d\x91~\\\xfd\xb1)m\xa6\xb3\x0c\x0b)\xb9\xd9:\xff\xfa\xd3\xa5\xac\x9a\xb7K\x15\xd9\ry\x17h\xfb\x19\xbf\x83\xb5\x8e\xcf\xc3\xb6\x9bU\x83@\x92\xc7\xb3\xddM\xab\x90\xc0g\xe9u\xccP2$\xed\x9cb\x99\xe9MN\x9fK\xd0\xe60@\x89AVJ\xe5S\xcf\x82=\xb9Ih\tD\xefK\'\x14\tm\x99s\xa7\x1b\xbd\xa3\xb3\xf7\xe7\xfd\x1d\x0cD\x92X\xe1\xdd\xafQ\x90\x15\x85\x183\xc3-v\x89\x11x\xc8e@\x0c\xb9\x9eO\xe9<\xa7\xfc\xec\xa2\xf1\x9e\x90\xff\x03\xe2\x9b=\xb4\xef\xd2\r\x04\xd8k\x105\x13\xb2\x1c\xc6\xf8\xdc\xba\xab\x13sd\x8dHC\x06\x87\x8a\x84R\x84\xb2\xa6\xbeO.}\x9f\x88\xc8R\x91#Daa\xf5\xa1\xbc|8\xea\x89\x92\xee?\x02?\xc0/\xd4L\xf7\x97\xec\xa4\x0c\xd2\xc4\xf2\xf1\x8fJO\xb7\\?\x89Wa\x9c\x1f\xe0\x14\xa8@K:\x03l\xac\xbc\xe8\xce\xd1\x06\x8b\xa8\xd7k&\xd6\xfe\x05Y\xce\xdc2\xf1\x0b\xdd\xbc\x833S\xa1\x08\xdd\xf7\xb0\xe4;:\xbd\xf3\xec\xf5*\x1e\xb8m\xccE\x15\xbd\x83\x9ed>O\x8a\xa2\x07\x94y\xbb\xde/\xe7gWct#:\x84\x86ab\xa8\x92\xd9))\x1d\x92Q\xb1\x1b\x96\x12\xab\xec\x00\xfab|aw\xe1\xcf\x1e\xe4!8\xf7\x96\xa2\x9f\xb5l\x8f\x05;/E\\<\x01\xa5\xf4\x82\xa1%\xcb\x16\xac8\xee\xbd\x8e\xe5\xb2\xcaG\x8a\x10]TS\x0el\xcd?\xff\xce@\xc0\xa0\xb9~\xfb-\x9by\x84\x86\xcd\xbbc\x93\x80)\x9fX\xb1 ,H\x1f\xf0\x80\x1b\xc8\\\x17\xe0\xb2T;TC\n(\xb1\xb3\xc1\xe4 \x1b6\xdbn\xe8J\xa2\xb3a\xab\xc0]D\xe28\x0et\xad&\xb9\xea!\xe3!\xd4/\x86\x9eI\x06|\x1av\xa11\xac\xbd\x19\xfe\xad\x9b\t\xf0\xc5\x92\xc2\xb8f\xf2\xc6X*\x1c`\xb8\x9c}1\xf1\xd8l\x11;:\x14\xb5L\xe2\xd2\xbfy\xa3\xfd\xf4\xe5\x18\xb8\xb42B\xadi\xeb\x03\xd6\x9bX\xfc\x8c\xf4\xc4\x8c\xb30\xfa*\xd2\x16\xf7\x8esTN)\xf0\xda\x89\x12\x8b\xac\xfa\xc9\xba\xaf\xe5\xda\xc1b\xf8\xceS1}\xf2\xee\x8d&$\xef\xd8\x8f9\xf1\x9a\x84\x8f\x90ny|\xe4\xa3l1\x18f\xbb\xfb\xad\xd9\x08\x88n|~\x83\xa3<V\xf4\xa0z\xb5ew\x15\x08\t\xe2\x0b\xec\xecD\x91\x0f\xd5ItB\x030\x1d\x1a!\xdc\x15\xcc\xa9q\x93\x86\xfafWm\xd2V\xf8\xba\x92\'\xe0\xbd\xa1\x14\x1a:\x0b\xa2~\x05qN\x19\xe1\x00\xa5\x90\xee[\xf8\xe9\x9b/\xae\xdd.\x11\x88\xc1[ )/w\x7f\xcc7\x93iKQ=\x1c?\xf4\xe5\x08B\x19=m\xf5\xd6\xd5\xb3\xae\xe6\xb1\xe8\xd9\x82LY\x83\x1fL\xa5\xe7\x03q\xf6\x06d\xe0\xc7\xe3\xe0Pg\rc\x05\xa6\xce\x83\x12\xccY\xc0*\x0cD\xfb&\xee\xcb\xdcd\xa6"\xb6\xba\xd8\x0c\xae<\xf921d\x84*\xd6\x14B^Z5\xa2\xbf\xadau\xa6g\x07\xee\xd4-:l\xa5\x15h\xc0H\x8e\x0e\x02/\x02\xbei\xb91$/\x12\xedi\xbd\x9aB\x01\x8et\xa6f\x87\xf7f\t\x91\xaf\x1e\xa4\x11\xe4\xf2nF"\x9a%\xd3\x80\xea^W\x1e\xccV\x9an\xdd\x92\xae\xb1H\xae#W\x85qo\xf3ES\x18\xde\x7f\xf7\xbc\xab\xca\xf5\t\x1dA\xe5\xf1\xe1n\x8a\xbe\t\xe0\xcd4\x99\xa7\xabr\xf09\x98:9\x8cR\xa4\xf9\x0f\x1a\x05\x93\r\x00C\xa6,\x9eY\xe8\xb5x\xfc\xe4%\xf6\x05}\xedJ\x94r\x805\xa5\xbe\x8d\x97\x19\xe0L\xfb\xc4\xd0\x88\xcb$\xcaZ\x0c\xeb\xe7l\x1c\x10\xbd\xc4\x86\x00\xfb\xa4\x95$\xa0\xcb&\x06\x9f\x9eM\xcf\xa4\x11\x1a\xce\xc4^\xdd\x08\xabbr\xa3^\xfb\xd8^xZ\x92\xa2\xd53b\x04-\x076.\xc6p\xf5I\xad\x1c\xde\x1f\xf5\t\xc6\xa66\x181y\x8b\xe8$\x15\xae\xec\xd2\x983\x81:?\xc8\x0e\xe1|\xbe\xebU\x03\xfa\x082B\xea\x16\xac\xa9\x04\xf7\xc6\xcb\xf8\xf7\xfd\xe7\x9b\xccd^\xdf3\x08\xa4\xceI\x0e\x8f\xb7\xc5\x1b\x87\nH\x96\xf0\xee^7\x00N\x83+C\x9f0\xda\xb2\x18B\x1a<c\xcd\xadex\xba\xac\xbc\x1a\xe0\x94\xcf\xcf\xae\xbd*\xd0?\xdd\x90m\r\x8c\t\xd2\xf24\xbc\xc7g\xe1\x03\x9f)\x011\xb2\x1a\xcd\x7fG\xee.\xe4\x8ap\xa1 @\xacp\x9c')))
except KeyboardInterrupt:
	exit()