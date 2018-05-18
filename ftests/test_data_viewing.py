from .base import FunctionalTest

class PdbPageTests(FunctionalTest):

    def test_pdb_page_layout(self):
        # User goes to PDB page
        self.get("/pdbs/A001/")
        self.check_title("A001")
        self.check_h1("A001")

        # There is information about the PDB
        pdb_information = self.browser.find_element_by_id("pdb-information")
        self.assertIn("A SUPERB PDB", pdb_information.text)
        self.assertIn("Deposited: 28 September, 1990", pdb_information.text)
        self.assertIn("Classification: REDUCTASE", pdb_information.text)
        self.assertIn("Technique: X-RAY", pdb_information.text)
        self.assertIn("Source Organism: Felis catus", pdb_information.text)
        self.assertIn("Expression System: Escherichia coli BL21(DE3)", pdb_information.text)
        self.assertIn("Resolution: 2.1", pdb_information.text)
        self.assertIn("R-factor: 4.5", pdb_information.text)
