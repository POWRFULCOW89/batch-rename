from main import scanDir, renameFiles
import unittest
from os import mkdir, rmdir
from os.path import exists
from shutil import rmtree

class TestBatchRename(unittest.TestCase):

    def test_a_createFiles(self):
        if not exists("tests"): mkdir("tests")
        for _ in range(5):
            with open('tests/' + "DummyFileNumber" + str(_) + '.txt', 'w') as f:
                f.write(str(_))
        self.assertTrue(exists("tests"))
        

    def test_b_scanFullDir(self):
        files = scanDir("./tests")
        self.assertEqual(files, ['DummyFileNumber0.txt',
            'DummyFileNumber1.txt',
            'DummyFileNumber2.txt',
            'DummyFileNumber3.txt',
            'DummyFileNumber4.txt'])

    def test_c_scanEmptyDir(self):
        if not exists("test_empty"): mkdir("test_empty")
        if not exists("test_empty/folder"): mkdir("test_empty/folder")
        files = scanDir("test_empty")
        self.assertIsNone(files)
        rmdir("test_empty/folder")
        rmdir("test_empty")
        

    def test_d_scanFakeDir(self):
        files = scanDir("money")
        self.assertIsNone(files)
        
    def test_e_scanFile(self):
        files = scanDir("/main.py")
        self.assertIsNone(files)

    # renameFiles(path, files, substring, new_string, numbers)
    def test_f_rename(self):
        files = scanDir("./tests")
        count = renameFiles("./tests", files, "Dummy", "", False )
        files = scanDir("./tests")
        self.assertEqual(files, 
        [   'FileNumber0.txt',
            'FileNumber1.txt',
            'FileNumber2.txt',
            'FileNumber3.txt',
            'FileNumber4.txt'])
        self.assertEqual(count, 5)

    def test_g_replace(self):
        files = scanDir("./tests")
        count = renameFiles("./tests", files, "File", "Archive", False )
        files = scanDir("./tests")
        self.assertEqual(count, 5)
        self.assertEqual(files, 
        [   'ArchiveNumber0.txt',
            'ArchiveNumber1.txt',
            'ArchiveNumber2.txt',
            'ArchiveNumber3.txt',
            'ArchiveNumber4.txt'])

    def test_h_rename_numerically(self):
        files = scanDir("./tests")
        count = renameFiles("./tests", files, "File_case_number_", "", True )
        files = scanDir("./tests")
        self.assertEqual(count, 5)
        self.assertListEqual(files, 
        [   'File_case_number_1.txt',
            'File_case_number_2.txt',
            'File_case_number_3.txt',
            'File_case_number_4.txt',
            'File_case_number_5.txt'])

    def test_i_failed_rename(self):
        files = scanDir("./tests")
        count = renameFiles("./tests", files, "Archive", "", False )
        files = scanDir("./tests")
        self.assertEqual(count, None)
        self.assertListEqual(files, 
        [   'File_case_number_1.txt',
            'File_case_number_2.txt',
            'File_case_number_3.txt',
            'File_case_number_4.txt',
            'File_case_number_5.txt'])

    def test_j_failed_rename_2(self):
        count = renameFiles("./test_fake", scanDir("./test_fake"), "throw", "away", True)
        files = scanDir("./test_fake")
        self.assertEqual(count, None)
        self.assertEqual(files, None)

    def test_k_rename_numerically_with_new_string(self):
        files = scanDir("./tests")
        count = renameFiles("./tests", files, "File_", "This doesnt matter", True )
        files = scanDir("./tests")
        self.assertEqual(count, 5)
        self.assertListEqual(files, 
        [   'File_1.txt',
            'File_2.txt',
            'File_3.txt',
            'File_4.txt',
            'File_5.txt'])
        
    def test_z_deleteFiles(self):
        rmtree("tests")
        # help(scanDir)
        # help(renameFiles)

if __name__ == '__main__':
    unittest.main()
