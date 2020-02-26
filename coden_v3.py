#THIS version can produce AA_sequence files,but their content is void.
#！coding:utf-8
#author:XieCuinanCAU
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
}#准备密码子表

with open('/Users/Xiecuinan/projects/jiaxuegene/ALK/ALK_test_coding_sequence.txt') as f:
    sequence = f.read()

file_name = 'ALK_{}_mutation_nuclioside_{}_to_{}.txt'
for i in range(len(sequence)):
    
    sequence_list = list(sequence)
    sequence_list[i] = 'A'
    new_seq = ''.join(sequence_list)
    rna_seq = new_seq.replace('T', 'U')#把T替换成U
    rna_seq_str = str(rna_seq)
    print (rna_seq_str)
    start_codon = 'AUG'#找起始密码子AUG，AUG及之后的序列作为编码rna
    start = rna_seq_str.find(start_codon)
    print (start)
    coding_rna = rna_seq[start:]
    print (coding_rna)
    AA_seq = []
    for n in (0, len(coding_rna), 3):
        
        if coding_rna[n:n+3] in coden_dict:
            AA_seq += list(coden_dict[coding_rna[n:n+3]])#编码rna每3个字母一组，去密码子表里匹配氨基酸，
            n = n + 3
            with open(file_name.format('AA_sequence',i,"A"),'w+') as aa:#准备一个文件，用来存变异后的氨基酸序列，文件名字应该随着变异位点改变而改变
                aa.write(str(AA_seq))#把氨基酸序列写进文件
                print ('New AA sequence is saved in:' + file_name.format('AA_sequence',i,"A"))#在电脑屏幕显示文件名
                import os
                print (file_name.format('AA_sequence',i,'A')+' is in:' + os.path.abspath('.'))#在电脑屏幕显示文件位置
        
        next


    fn = file_name.format('coding_sequence',i,"A")
    fo = open(fn,'w+')
    fn = fo.writelines(str(new_seq))
    i = i+1
    print ('New coding sequence is saved in:' + file_name.format('coding_sequence',i,"A"))
    import os
    print (file_name.format('coding_sequence',i,'A')+' is in:' + os.path.abspath('.'))
    #Here file name is fn's name,but cannot use 'fn' to avoid print fn's content.
    next


