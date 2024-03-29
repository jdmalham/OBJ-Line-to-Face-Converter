import time

start = time.time()

object_file = r'C:\Users\Owner\Desktop\Functional Scripts\OBJ Files\Tracks_V3.obj'

def obj_multi_line_mod(path):
    path_list = path.split('\\')
    file_name = path_list[-1].split('.')[0]
    with open(path,'r') as finp, open(f'mod_{file_name}.obj','w') as fout:
        n = 0
        #the exclusion list allows us to disconnect the faces from one another
        exclusion_index_list = []
        contents = finp.readlines()
        new_contents = []
        for index, line in enumerate(contents):
            #read through the file line by line
            if line[0:2] != 'l ':
                #check to see if the line is a line declaration
                new_contents.append(line)
            else:
                #in which case, take note of which index needs to be added to the exclusion list
                if n != 0:
                    exclusion_index_list.append((n*2)-1)
                continue
            if line[0:2] == 'v ':
                #find all vertex values in the file and create a copy of the line
                #with y offset +0.1
                vertex_string = line
                coordinates = vertex_string.split(' ')
                new_y = str(float(coordinates[2])+0.01)
                new_vertex = f'v {coordinates[1]} {new_y} {coordinates[3]}'
                new_contents.append(new_vertex)
                n += 1
        i=1
        while i < (2*n)-1:
            if i in exclusion_index_list:
                i+=2
                continue
            new_face = f'f {i} {i+1} {i+3} {i+2}\nf {i+2} {i+3} {i+1} {i}\n'
            new_contents.append(new_face)
            i+=2
        #print(new_contents)
        fout.writelines(new_contents)
        
obj_multi_line_mod(object_file)

end = time.time()

print(str(end-start))
