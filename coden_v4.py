#THIS version can produce AA_sequence files,but their content is void.
#！coding:utf-8
#author:XieCuinanCAU
def conden( ):
    coden_dict = {
    'UUU':'F','UUC':'F','UUA':'L','UUG':'L',
    'CUU':'L','CUC':'L','CUA':'L','CUG':'L',
    'AUU':'I','AUC':'I','AUA':'I','AUG':'M',
    'GUU':'V','GUC':'V','GUA':'V','GUG':'V',

    'UCU':'S','UCC':'S','UCA':'S','UCG':'S',
    'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACU':'U','ACC':'U','ACA':'U','ACG':'U',
    'GCU':'A','GCC':'A','GCA':'A','GCG':'A',

    'UAU':'Y','UAC':'Y','UAA':'*','UAG':'*',
    'CAU':'H','CAC':'H','CAA':'H','CAG':'H',
    'AAU':'N','AAC':'N','AAA':'K','AAG':'K',
    'GAU':'D','GAC':'D','GAA':'E','GAG':'E',

    'UGU':'C','UGC':'C','UGA':'*','UGG':'W',
    'CGU':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGU':'S','AGC':'S','AGA':'R','AGG':'R',
    'GGU':'G','GGC':'G','GGA':'G','GGG':'G',
    }#准备好密码子表

file_name = 'ALK_{}_mutation_nuclioside_{}_to_{}.txt'
with open('/Users/Xiecuinan/projects/jiaxuegene/ALK/ALK_test_coding_sequence.txt') as f:
    sequence = f.read()

def transcription( ):
    for i in range(len(sequence)):
    
        sequence_list = list(sequence)
        sequence_list[i] = 'A'
        new_seq = ''.join(sequence_list)
        rna_seq = new_seq.replace('T', 'U')#把T替换成U
        rna_seq_str = str(rna_seq)
        #print (rna_seq_str)
        start_codon = 'AUG'#找起始密码子AUG，AUG及之后的序列作为编码RNA序列
        start = rna_seq_str.find(start_codon)
        #print (start)
        coding_rna = rna_seq[start:]
        #print (coding_rna)
        AA_seq = []
        next
def translate( ):
    for n in (0, len(coding_rna), 3):
        if coding_rna[n:n+3] in coden_dict:
            AA_seq +=list(coden_dict[coding_rna[n:n+3]])
                #编码RNA每3个字母一组，和密码子匹配，找对应的氨基酸代号
            n = n + 3
            with open(file_name.format('AA_sequence',i,"A"),'w+') as aa:#准备一个文件，用来存变异后的氨基酸序列，文件名字应该随着变异位点改变而改变
                aa.write(str(AA_seq))#把氨基酸序列写进文件
                aafn = file_name.format('AA_sequence',i,"A")
                print ('New AA sequence is saved in:' + aafn)
                #在电脑屏幕显示每个氨基酸序列的文件名

                import os
                print (file_name.format('AA_sequence',i,'A')+' is in:' + os.path.abspath('.'))#在电脑屏幕显示氨基酸序列的文件位置
        
        next
    return aafn


def mutation( ):
    fn = file_name.format('coding_sequence',i,"A")
    fo = open(fn,'w+')
    fn = fo.write(str(new_seq))
    i = i+1
    print ('New coding sequence is saved in:' + fn)
    import os
    print (file_name.format('coding_sequence',i,'A')+' is in:' + os.path.abspath('.'))
    return fn
#Here file name is fn's name,but cannot use 'fn' to avoid print fn's content.


     
