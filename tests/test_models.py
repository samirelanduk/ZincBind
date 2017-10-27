from datetime import datetime
from mixer.backend.django import mixer
from django.core.exceptions import ValidationError
from unittest.mock import patch, Mock, MagicMock
from .base import ZincBindTest
from zincbind.models import Pdb, Residue, Atom, ZincSite

class PdbTests(ZincBindTest):

    def test_can_create_pdb(self):
        pdb = Pdb(
         pk="1XXY", title="The PDB Title", deposited="1990-09-28",
         resolution=4.5, checked="2017-01-01"
        )
        self.assertEqual(pdb.residue_set.count(), 0)
        pdb.full_clean()


    def test_title_is_required(self):
        pdb = Pdb(
         pk="1XXY", title=None, deposited="1990-09-28",
         resolution=4.5, checked="2017-01-01"
        )
        with self.assertRaises(ValidationError):
            pdb.full_clean()
        pdb = Pdb(
         pk="1XXY", title="", deposited="1990-09-28",
         resolution=4.5, checked="2017-01-01"
        )
        with self.assertRaises(ValidationError):
            pdb.full_clean()


    def test_date_is_required(self):
        pdb = Pdb(
         pk="1XXY", title="The PDB Title", deposited=None,
         resolution=4.5, checked="2017-01-01"
        )
        with self.assertRaises(ValidationError):
            pdb.full_clean()


    def test_resolution_is_required(self):
        pdb = Pdb(
         pk="1XXY", title="The PDB Title", deposited="1990-09-28",
         resolution=None, checked="2017-01-01"
        )
        with self.assertRaises(ValidationError):
            pdb.full_clean()
        pdb = Pdb(
         pk="1XXY", title="The PDB Title", deposited="1990-09-28",
         resolution=0, checked="2017-01-01"
        )
        pdb.full_clean()


    def test_checked_can_be_null(self):
        pdb = Pdb(
         pk="1XXY", title="The PDB Title", deposited="1990-09-28",
         resolution=4.5, checked=None
        )
        pdb.full_clean()



class ResidueTests(ZincBindTest):

    def setUp(self):
        ZincBindTest.setUp(self)
        self.pdb = mixer.blend(Pdb)


    def test_can_create_residue(self):
        residue = Residue(
         pk="1XYZA10", residue_id="A10", name="VAL", chain="A", number=10,
         pdb=self.pdb
        )
        self.assertEqual(residue.atom_set.count(), 0)
        self.assertEqual(residue.zincsite_set.count(), 0)
        residue.full_clean()


    def test_residueid_is_required(self):
        residue = Residue(
         pk="1XYZA10", residue_id=None, name="VAL", chain="A", number=10,
         pdb=self.pdb
        )
        with self.assertRaises(ValidationError):
            residue.full_clean()
        residue = Residue(
         pk="1XYZA10", residue_id="", name="VAL", chain="A", number=10,
         pdb=self.pdb
        )
        with self.assertRaises(ValidationError):
            residue.full_clean()


    def test_name_is_required(self):
        residue = Residue(
         pk="1XYZA10", residue_id="A10", name=None, chain="A", number=10,
         pdb=self.pdb
        )
        with self.assertRaises(ValidationError):
            residue.full_clean()
        residue = Residue(
         pk="1XYZA10", residue_id="A10", name="", chain="A", number=10,
         pdb=self.pdb
        )
        with self.assertRaises(ValidationError):
            residue.full_clean()


    def test_chain_is_required(self):
        residue = Residue(
         pk="1XYZA10", residue_id="A10", name="VAL", chain=None, number=10,
         pdb=self.pdb
        )
        with self.assertRaises(ValidationError):
            residue.full_clean()
        residue = Residue(
         pk="1XYZA10", residue_id="A10", name="VAL", chain="", number=10,
         pdb=self.pdb
        )
        with self.assertRaises(ValidationError):
            residue.full_clean()


    def test_number_is_required(self):
        residue = Residue(
         pk="1XYZA10", residue_id="A10", name="VAL", chain="A", number=None,
         pdb=self.pdb
        )
        with self.assertRaises(ValidationError):
            residue.full_clean()
        residue = Residue(
         pk="1XYZA10", residue_id="A10", name="VAL", chain="A", number=0,
         pdb=self.pdb
        )
        residue.full_clean()


    def test_pdb_is_required(self):
        residue = Residue(
         pk="1XYZA10", residue_id="A10", name="VAL", chain="A", number=10,
         pdb=None
        )
        with self.assertRaises(ValidationError):
            residue.full_clean()



class AtomTests(ZincBindTest):

    def setUp(self):
        ZincBindTest.setUp(self)
        self.residue = mixer.blend(Residue)


    def test_can_create_atom(self):
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=1.5, y=-1.5, z=0.0,
         element="C", charge=-1, bfactor=13.4, residue=self.residue
        )
        atom.full_clean()


    def test_atomid_is_required(self):
        atom = Atom(
         pk="1XYZ555", atom_id=None, name="CA", x=1.5, y=-1.5, z=0.0,
         element="C", charge=-1, bfactor=13.4, residue=self.residue
        )
        with self.assertRaises(ValidationError):
            atom.full_clean()
        atom = Atom(
         pk="1XYZ555", atom_id=0, name="CA", x=1.5, y=-1.5, z=0.0,
         element="C", charge=-1, bfactor=13.4, residue=self.residue
        )
        atom.full_clean()


    def test_name_is_required(self):
        atom = Atom(
         pk="1XYZ555", atom_id=555, name=None, x=1.5, y=-1.5, z=0.0,
         element="C", charge=-1, bfactor=13.4, residue=self.residue
        )
        with self.assertRaises(ValidationError):
            atom.full_clean()
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="", x=1.5, y=-1.5, z=0.0,
         element="C", charge=-1, bfactor=13.4, residue=self.residue
        )
        with self.assertRaises(ValidationError):
            atom.full_clean()


    def test_x_is_required(self):
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=None, y=-1.5, z=0.0,
         element="C", charge=-1, bfactor=13.4, residue=self.residue
        )
        with self.assertRaises(ValidationError):
            atom.full_clean()
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=0, y=-1.5, z=0.0,
         element="C", charge=-1, bfactor=13.4, residue=self.residue
        )
        atom.full_clean()


    def test_y_is_required(self):
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=1.5, y=None, z=0.0,
         element="C", charge=-1, bfactor=13.4, residue=self.residue
        )
        with self.assertRaises(ValidationError):
            atom.full_clean()
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=1.5, y=0, z=0.0,
         element="C", charge=-1, bfactor=13.4, residue=self.residue
        )
        atom.full_clean()


    def test_z_is_required(self):
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=1.5, y=-1.5, z=None,
         element="C", charge=-1, bfactor=13.4, residue=self.residue
        )
        with self.assertRaises(ValidationError):
            atom.full_clean()
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=1.5, y=-1.5, z=0,
         element="C", charge=-1, bfactor=13.4, residue=self.residue
        )
        atom.full_clean()


    def test_element_is_required(self):
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=1.5, y=-1.5, z=0.0,
         element=None, charge=-1, bfactor=13.4, residue=self.residue
        )
        with self.assertRaises(ValidationError):
            atom.full_clean()
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=1.5, y=-1.5, z=0.0,
         element="", charge=-1, bfactor=13.4, residue=self.residue
        )
        with self.assertRaises(ValidationError):
            atom.full_clean()


    def test_charge_is_required(self):
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=1.5, y=-1.5, z=0.0,
         element="C", charge=None, bfactor=13.4, residue=self.residue
        )
        with self.assertRaises(ValidationError):
            atom.full_clean()
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=1.5, y=-1.5, z=0.0,
         element="C", charge=0, bfactor=13.4, residue=self.residue
        )
        atom.full_clean()


    def test_bfactor_is_required(self):
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=1.5, y=-1.5, z=0.0,
         element="C", charge=-1, bfactor=None, residue=self.residue
        )
        with self.assertRaises(ValidationError):
            atom.full_clean()
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=1.5, y=-1.5, z=0.0,
         element="C", charge=-1, bfactor=0, residue=self.residue
        )
        atom.full_clean()


    def test_residue_is_required(self):
        atom = Atom(
         pk="1XYZ555", atom_id=555, name="CA", x=1.5, y=-1.5, z=0.0,
         element="C", charge=-1, bfactor=13.4, residue=None
        )
        with self.assertRaises(ValidationError):
            atom.full_clean()



class ZincSiteTests(ZincBindTest):

    def test_can_create_zinc_site(self):
        site = ZincSite(pk="1ZZZA500", x=1.5, y=-1.5, z=10.0)
        self.assertEqual(site.residues.count(), 0)
        site.full_clean()


    def test_x_is_required(self):
        site = ZincSite(pk="1ZZZA500", x=None, y=-1.5, z=10.0)
        with self.assertRaises(ValidationError):
            site.full_clean()
        site = ZincSite(pk="1ZZZA500", x=0, y=-1.5, z=10.0)
        site.full_clean()


    def test_y_is_required(self):
        site = ZincSite(pk="1ZZZA500", x=0, y=None, z=10.0)
        with self.assertRaises(ValidationError):
            site.full_clean()
        site = ZincSite(pk="1ZZZA500", x=1.5, y=0, z=10.0)
        site.full_clean()


    def test_z_is_required(self):
        site = ZincSite(pk="1ZZZA500", x=1.5, y=-1.5, z=None)
        with self.assertRaises(ValidationError):
            site.full_clean()
        site = ZincSite(pk="1ZZZA500", x=1.5, y=-1.5, z=0.0)
        site.full_clean()