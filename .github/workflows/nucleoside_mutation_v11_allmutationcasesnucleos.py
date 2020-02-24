#！coding:utf-8
#author:XieCuinanCAU
#global old_sequence

with open('d:/XCN_script/test_ALK_test/ALK_test_coding_sequence.txt') as f:
    sequence = f.read()

file_name = 'ALK_gene_mutation_nuclioside_{}_to_{}.txt'
for i in range(len(sequence)):
    
    sequence_list = list(sequence)
    sequence_list[i] = 'A'
    new_seq = ''.join(sequence_list)

    fn = file_name.format(i,"A")
    fo = open(fn,'w+')
    fn = fo.writelines(str(new_seq))
    i = i+1
    print ('New gene sequence is saved in:' + file_name.format(i,"A"))
    import os
    print (file_name.format(i,'A')+' is in:' + os.path.abspath('.'))
    next

for i in range(len(sequence)):
    
    sequence_list = list(sequence)
    sequence_list[i] = 'G'
    new_seq = ''.join(sequence_list)

    fn = file_name.format(i,'G')
    fo = open(fn,'w+')
    fn = fo.writelines(str(new_seq))
    i = i+1
    print ('New gene sequence is saved in:' + file_name.format(i,"G"))
    import os
    print (file_name.format(i,'G')+' is in:' + os.path.abspath('.'))
    next

for i in range(len(sequence)):
    
    sequence_list = list(sequence)
    sequence_list[i] = 'C'
    new_seq = ''.join(sequence_list)

    fn = file_name.format(i,'C')
    fo = open(fn,'w+')
    fn = fo.writelines(str(new_seq))
    i = i+1
    print ('New gene sequence is saved in:' + file_name.format(i,'C'))
    import os
    print (file_name.format(i,'C')+' is in:' + os.path.abspath('.'))
    next

for i in range(len(sequence)):
    
    sequence_list = list(sequence)
    sequence_list[i] = 'T'
    new_seq = ''.join(sequence_list)

    fn = file_name.format(i,'T')
    fo = open(fn,'w+')
    fn = fo.writelines(str(new_seq))
    i = i+1
    print ('New gene sequence is saved in:' + file_name.format(i,'T'))
    import os
    print (file_name.format(i,'T')+' is in:' + os.path.abspath('.'))
    next











