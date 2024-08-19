#[1] creating a dummy text file
f = open('[19]Modules/filename.txt', 'w')
f.write('zip this textfile')
f.close()

f = open('[19]Modules/filename2.txt', 'w')
f.write('zip this textfile')
f.close()

#[2] zipping individual file
import zipfile

comp_file = zipfile.ZipFile('[19]Modules/comp_file.zip', 'w')

comp_file.write('[19]Modules/filename.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('[19]Modules/filename2.txt', compress_type=zipfile.ZIP_DEFLATED)

comp_file.close()

#[3] unzipping the files
zip_obj = zipfile.ZipFile('[19]Modules/comp_file.zip', 'r')

zip_obj.extractall('[19]Modules/extracted_content')












