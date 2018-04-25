import glob
import os
import shutil
import re
path = '/Users/clairhu/dev/dl'
# for filename in glob.glob(os.path.join(path, '*.ipynb')):/Users/clairhu/dev/dl/solution1/deeplearinig.ai-course-solutions
#    print (filename)/Users/clairhu/dev/dl/solution2/deeplearning.ai/COURSE 3 Structuring Machine Learning Projects
# /Users/clairhu/dev/dl/solution2/deeplearning.ai/Users/clairhu/dev/dl/solution2/deeplearning.ai/COURSE 5 Sequence Model/Week1
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".ipynb"):
            base_file_path = os.path.join(root, file)
            move_dir_path = re.sub(r'solution\d+/deep.*?/', 'Assignment/', root)
            # # move_dir_path = root.replace('solution/deeplearinig.ai', 'Assignments')
            file = os.path.join(root, file)
            file = re.sub(r'solution\d+/deep.*?/', 'Assignment/', file)
            # # file = os.path.join(root, file).replace('solution3/deeplearinig.ai', 'Assignments')
            if not os.path.exists(move_dir_path):
                os.makedirs(move_dir_path)
                os.chmod(move_dir_path, 0o777)
            if not os.path.exists(file):
            	shutil.copy(base_file_path, file)
            toDelete = False
            out = open(file,'r')
            lines = out.readlines()
            out.close()
            out = open(file,'w')
            t=[]
            for line in lines:
                if "START CODE HERE" in line:
                    toDelete = True
                    t.append(line)
                    t.append("\n")
                else:
                	if "#" in line and '##' not in line and True == toDelete:
                		# print(line)
                		line =  line.split('#')[1]
                		line = '\"' + '            #' + line
                		# print(line)
                		t.append(line)
                		t.append("\n")
                if "END CODE HERE" in line:
                    toDelete = False 
                if False == toDelete:
                    t.append(line)
            out.writelines(t)   
            out.close()
        else:
        	base_file_path = os.path.join(root, file)
	        move_dir_path = re.sub(r'solution\d+/deep.*?/', 'Assignment/', root)
	        # # move_dir_path = root.replace('solution/deeplearinig.ai', 'Assignments')
	        file = os.path.join(root, file)
	        file = re.sub(r'solution\d+/deep.*?/', 'Assignment/', file)
	        # # file = os.path.join(root, file).replace('solution3/deeplearinig.ai', 'Assignments')
	        if not os.path.exists(move_dir_path):
	            os.makedirs(move_dir_path)
	            os.chmod(move_dir_path, 0o777)
	        if not os.path.exists(file):
	            try:
	                shutil.copy(base_file_path, file)
	            except FileNotFoundError:
	         	   print("not found")



