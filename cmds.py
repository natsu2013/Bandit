solutions = {
    'level0': [b'cat readme'],
    'level1': [b'cat ./-'],
    'level2': [b'cat spaces\\ in\\ this\\ filename'],
    'level3': [b'cd inhere/', b'cat .hidden'],
    'level4': [b'cd inhere/', b'find . | xargs file | grep ASCII | cut -d ":" -f 1 | xargs cat'],
    'level5': [b'cd inhere/', b'find . -type f -size 1033c | xargs cat'],
    'level6': [b'find / -user bandit7 -group bandit6 -size 33c 2>&1 | grep -v  -e \'Permission denied\' -e \'No such\' | xargs cat'],
    'level7': [b'cat data.txt | grep \'millionth\' | cut -f 2'],
    'level8': [b'sort data.txt | uniq -u'],
    'level9': [b'strings data.txt | grep \'&=\' | cut -d " " -f 2'],
    'level10': [b'base64 -d data.txt | cut -d \' \' -f 4'],
    'level11': [b'cat data.txt | tr \'A-Za-z\' \'N-ZA-Mn-za-m\' | cut -d \' \' -f 4'],
    'level12': [
        b'export D=/tmp/level12',
        b'if [[ -d $D  ]]; then rm -rf /tmp/level12; fi',
        b'mkdir /tmp/level12', 
        b'cp data.txt /tmp/level12', 
        b'cd /tmp/level12', 
        b'xxd -r data.txt > data', 
        b'mv data file.gz',
        b'gzip -d file.gz',
        b'mv file file.bz2',
        b'bzip2 -d file.bz2',
        b'mv file file.gz',
        b'gzip -d file.gz',
        b'mv file file.tar',
        b'tar xf file.tar',
        b'mv data5.bin data5.tar',
        b'tar xf data5.tar',
        b'mv data6.bin data6.bz2',
        b'bzip2 -d data6.bz2',
        b'mv data6 data6.tar',
        b'tar xf data6.tar',
        b'mv data8.bin data8.gz',
        b'gzip -d data8.gz',
        b'cat data8 | cut -d \' \' -f 4'
    ],
    'level13': [b'ssh bandit14@localhost -i sshkey.private', b'yes', b'cat /etc/bandit_pass/bandit14'], #4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
    'level14': [b'echo "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e" | nc localhost 30000  | sed -n 2p'], #sed -n -e '2{p;q}'
    # 'level15': [b'echo BfMYroe26WYalil77FoDi9qh59eK5xNr | openssl s_client -quiet -connect localhost:30001 | tail -n 2'], #cluFn7wTiGryunymYOu4RcffSxQluehd
    'level15': [b'echo cluFn7wTiGryunymYOu4RcffSxQluehd'],
    # 'level16': [b'echo '],
    # 'level17': [b'echo '],
    # 'level18': [b'echo '],
    # 'level19': [b'echo '],
    # 'level20': [b'echo '],
    # 'level21': [b'echo '],
    # 'level22': [b'echo '],
    # 'level23': [b'echo '],
    # 'level24': [b'echo '],
}


# sed 
# tail 
# awk 


