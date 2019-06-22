from prev_ob_models.utils import RunInClassDirectory, IsolatedCell
import os, sys

class OlfactoryBulbCell(IsolatedCell):
    def __init__(self, cell_id):
        self.cell_id = str(cell_id)

        with RunInClassDirectory(OlfactoryBulbCell):
            # Load the channels
            os.chdir("Mechanisms")
            from neuron import h#, gui
            os.chdir("..")

            h.load_file("stdrun.hoc")
            h.celsius = 35
            h.cvode_active(1)

            # Load the cell HOC file (they follow MC1.hoc, GC1.hoc, ... pattern)
            os.chdir("Cells")
            self.hoc_path = os.path.abspath(self.cell_type + str(cell_id) + ".hoc")
            h.load_file(self.hoc_path)
            os.chdir("..")

            # Build the cell
            self.hoc_template = self.cell_type + str(cell_id)
            self.cell = getattr(h, self.hoc_template)()
            self.h = h
            self.soma = self.cell.soma

    def set_model_params(self, param_values):
        from neuron import h

        # The diam param functions as a scaling factor of the existing diameters
        # to be able to set the params multiple times, the original diams need to be used when multiplying
        # Here, this is done by instantiating an unmodified copy of the cell
        unmodified_cell = getattr(h, self.hoc_template)()

        for pi, pv in enumerate(param_values):
            attr = self.params[pi]["attr"]
            if attr == "tau_CaPool":
                setattr(h, attr, pv)
            else:
                for param_list in self.params[pi]["lists"]:
                    if not hasattr(self.cell, param_list):
                        print("List",param_list, "not found in cell", self.hoc_template, "Skipping list...")
                        continue

                    if attr == "diam":
                        unmodified_secs = [sec for sec in getattr(unmodified_cell, param_list)]

                    for isec, sec in enumerate(getattr(self.cell, param_list)):
                        if attr == "diam":
                            for i3d in range(int(h.n3d(sec=sec))):
                                orig_diam = h.diam3d(i3d, sec=unmodified_secs[isec])
                                h.pt3dchange(i3d, orig_diam * pv, sec=sec)
                        else:
                            setattr(sec, attr, pv)

        del unmodified_cell

class MC(OlfactoryBulbCell):

    # Parameters and their ranges used for fitting
    params = [
        {"attr": "diam", "low": 0.1, "high": 5.0, "lists": ["apical", "basal", "axonal"]},
        {"attr": "Ra", "low": 1.0, "high": 150.0, "lists": ["all"]},
        {"attr": "cm", "low": 0.1, "high": 2.0, "lists": ["all"]},
        {"attr": "ena", "low": 20.0, "high": 80.0, "lists": ["all"]},
        {"attr": "ek", "low": -100.0, "high": -50.0, "lists": ["all"]},
        {"attr": "e_pas", "low": -90.0, "high": -50.0, "lists": ["all"]},
        {"attr": "g_pas", "low": 0, "high": 0.00004, "lists": ["all"]},
        {"attr": "sh_Na", "low": 0, "high": 10, "lists": ["all"]},
        {"attr": "tau_CaPool", "low": 1, "high": 300, "lists": ["all"]},

        {"attr": "gbar_Na", "low": 0, "high": 0.1, "lists": ["all"]},
        {"attr": "gbar_Kd", "low": 0, "high": 0.1, "lists": ["all"]},
        {"attr": "gbar_Kslow", "low": 0, "high": 0.001, "lists": ["all"]},
        {"attr": "gbar_KA", "low": 0, "high": 0.02, "lists": ["all"]},
        {"attr": "gbar_KCa", "low": 0, "high": 0.016, "lists": ["all"]},
        {"attr": "gbar_LCa", "low": 0, "high": 0.0005, "lists": ["all"]},

        {"attr": "eh", "low": -40.0, "high": -10.0, "lists": ["apical"]},
        {"attr": "gbar_Ih", "low": 0, "high": 0.000003, "lists": ["apical"]},
        {"attr": "gbar_CaT", "low": 0, "high": 20e-3, "lists": ["apical"]},
    ]

    cell_type = "MC"


class MC1(MC):
    def __init__(self):
        super(MC1, self).__init__(cell_id=1)
        self.param_values = [3.22389443491247, 2.81865928031078, 0.33261043003167834, 27.0037817821923, -64.93732914068036, -73.25204775921887, 2.1361316231147274e-05, 3.76535811520783, 4.308024855943862, 0.03186952629227804, 0.023795201285494796, 0.0007185750073984963, 0.002526117846022963, 0.0009455163544555489, 0.00016863361902873404, -36.099624268474926, 3.655648607819723e-07, 0.004428920251185234]
        self.set_model_params(self.param_values)

class MC2(MC):
    def __init__(self):
        super(MC2, self).__init__(cell_id=2)
        self.param_values = [2.3511459438710984,126.79240156883097,0.5169516132656169,36.70146443789503,-59.939258607150514,-63.44102868866163,2.508982638071978e-05,3.4858670343332308,7.507321595674958,0.013630971923446833,0.0011455738584287012,0.00038998349958084864,0.003250159154661294,0.0037771563959725,0.0004433261041866151,-15.91046573495657,1.816124175620452e-07,0.007912495290042867]
        self.set_model_params(self.param_values)

class MC3(MC):
    def __init__(self):
        super(MC3, self).__init__(cell_id=3)
        self.param_values =  [2.5423168283445956, 22.24438742171681, 0.6495059435075267, 25.514798622627445, -69.80712920166272, -57.42040781764916, 1.9476222649318898e-05, 4.343600147915433, 6.659410081345059, 0.04428811469036931, 0.014229735150034572, 0.0001648293604053363, 0.005382990776749325, 0.0012568660047021492, 0.00010974581311243848, -28.970056925719366, 6.455001190237628e-07, 0.002468829827979082]
        self.set_model_params(self.param_values)

class MC4(MC):
    def __init__(self):
        super(MC4, self).__init__(cell_id=4)
        self.param_values = [1.0882827660647931, 8.97791641084582, 0.6307453448260578, 44.81115966615397, -61.19341314098865, -72.77205927215527, 3.0005066359112136e-05, 1.2273167760473112, 8.57738871414464, 0.009745103588705815, 0.016814274105780822, 0.0008630161891010214, 0.0029899442463640303, 0.0017233830355042575, 0.0003758675164563642, -20.101758455718468, 9.699711091593169e-07, 0.0011559009225374898]
        self.set_model_params(self.param_values)

class MC5(MC):
    def __init__(self):
        super(MC5, self).__init__(cell_id=5)
        self.param_values = [1.2471592703753913, 89.54731666051053, 0.9576321104748539, 23.163661456098886, -63.438841110533915, -75.05751351034053, 3.657331273597089e-05, 2.6570771987427655, 9.666857483589407, 0.06150916169169841, 0.03759175148995797, 0.0004759847063037054, 0.0042226776511213, 0.00776370232830789, 9.599737738463663e-06, -16.369883529143777, 1.9500130790130927e-06, 0.01027446638931233]
        self.set_model_params(self.param_values)


class GC(OlfactoryBulbCell):

    # Parameters and their ranges used for fitting
    params = [
        { "attr": "diam",  "low": 0.1, "high": 3.0, "lists": ["apical"]},

        { "attr": "Ra",    "low": 5.0, "high": 120.0, "lists": ["all"]},
        { "attr": "cm",    "low": 0.1, "high": 10.0, "lists": ["all"]},
        { "attr": "ena",   "low": 10.0, "high": 50.0, "lists": ["all"]},
        { "attr": "ek",    "low": -100.0, "high": -30.0, "lists": ["all"]},
        { "attr": "e_pas", "low": -100.0, "high": -50.0, "lists": ["all"]},
        { "attr": "g_pas", "low": 0, "high": 0.0020, "lists": ["all"]},
        { "attr": "sh_Na", "low": 0, "high": 10, "lists": ["all"]},
        { "attr": "gbar_Na", "low": 0, "high": 0.1, "lists": ["all"]},
        { "attr": "gbar_Kd", "low": 0, "high": 0.4, "lists": ["all"]},

        { "attr": "gbar_KA", "low": 0, "high": 0.4, "lists": ["somatic"]},
        { "attr": "eh",      "low": -60.0, "high": -10.0, "lists": ["somatic"]},
        { "attr": "gbar_Ih", "low": 0, "high": 0.000100, "lists": ["somatic"]},
        { "attr": "gbar_KM", "low": 0, "high": 0.13, "lists": ["somatic"]},

    ]

    cell_type = "GC"

class GC1(GC):
    def __init__(self):
        super(GC1, self).__init__(cell_id=1)
        self.param_values = [1.143699798058159, 38.63588512122286, 1.3246244244225323, 21.644563058960998, -78.45958976794006, -84.176971627722, 3.523246101993713e-05, 4.806897287024132, 0.06430609559992095, 0.14763349696401334, 0.005483256218645492, -16.71808607677032, 1.1553874669375734e-06, 0.07033316111123607]
        self.set_model_params(self.param_values)

class GC2(GC):
    def __init__(self):
        super(GC2, self).__init__(cell_id=2)
        self.param_values = [0.518568993696911, 22.331096575385537, 3.9991551066170175, 44.54836939907614, -55.16528090080958, -89.29463560245307, 0.00018368809366833735, 2.776003601349153, 0.07465156310126753, 0.21211096020752224, 0.04941295865598961, -53.44113851681273, 2.548528534052994e-06, 0.006660630409332343]
        self.set_model_params(self.param_values)

class GC3(GC):
    def __init__(self):
        super(GC3, self).__init__(cell_id=3)
        self.param_values = [0.9269014411917871, 70.42171573661824, 1.971342274619708, 47.107745396041246, -60.5888373035133, -95.78092714858376, 6.0612146854136255e-05, 1.6251939756805538, 0.028139028565849572, 0.08172220519881213, 0.01960472171669605, -42.72464976323857, 4.056438596462772e-07, 0.003498922852414627]
        self.set_model_params(self.param_values)

class GC4(GC):
    def __init__(self):
        super(GC4, self).__init__(cell_id=4)
        self.param_values = [0.39560570044908316, 14.7001785531141, 5.603476105466056, 48.85341001832027, -59.13731541119851, -88.95055139135725, 0.00019849201601866652, 0.332377877393758, 0.09017983310353604, 0.3722082289291057, 0.020675866784401864, -29.718912591813137, 2.2674619647194348e-05, 0.0022058201031577435]
        self.set_model_params(self.param_values)

class GC5(GC):
    def __init__(self):
        super(GC5, self).__init__(cell_id=5)
        self.param_values = [0.6612176297384526, 58.094003958059446, 3.3943923884236686, 37.26904050043951, -49.50647388390325, -86.25711959382369, 9.692038669317667e-05, 8.307611212489611, 0.09335591754413584, 0.14722737230872723, 0.04182067505119284, -57.7385836483234, 6.56570790637639e-07, 0.001077740080191274]
        self.set_model_params(self.param_values)
        
        
        
class TC(OlfactoryBulbCell):

    # Parameters and their ranges used for fitting
    params = [
        {"attr": "diam", "low": 0.1, "high": 5.0, "lists": ["apical", "basal", "axonal"]},
        {"attr": "Ra", "low": 1.0, "high": 150.0, "lists": ["all"]},
        {"attr": "cm", "low": 0.1, "high": 5.0, "lists": ["all"]},
        {"attr": "ena", "low": 20.0, "high": 80.0, "lists": ["all"]},
        {"attr": "ek", "low": -100.0, "high": -50.0, "lists": ["all"]},
        {"attr": "e_pas", "low": -90.0, "high": -50.0, "lists": ["all"]},
        {"attr": "g_pas", "low": 0, "high": 0.00040, "lists": ["all"]},
        {"attr": "sh_Na", "low": 0, "high": 10, "lists": ["all"]},
        {"attr": "tau_CaPool", "low": 1, "high": 300, "lists": ["all"]},

        {"attr": "gbar_Na", "low": 0, "high": 0.1, "lists": ["all"]},
        {"attr": "gbar_Kd", "low": 0, "high": 0.1, "lists": ["all"]},
        {"attr": "gbar_Kslow", "low": 0, "high": 0.002, "lists": ["all"]},
        {"attr": "gbar_KA", "low": 0, "high": 0.02, "lists": ["all"]},
        {"attr": "gbar_KCa", "low": 0, "high": 0.016, "lists": ["all"]},
        {"attr": "gbar_LCa", "low": 0, "high": 0.0010, "lists": ["all"]},

        {"attr": "eh", "low": -40.0, "high": -10.0, "lists": ["apical"]},
        {"attr": "gbar_Ih", "low": 0, "high": 0.000030, "lists": ["apical"]},
        {"attr": "gbar_CaT", "low": 0, "high": 20e-3, "lists": ["apical"]},
    ]

    cell_type = "TC"


class TC1(TC):
    def __init__(self):
        super(TC1, self).__init__(cell_id=1)
        self.param_values = [2.7304441858755872, 91.64110821186408, 0.7497387007706371, 36.83597833861246, -66.26684277503126, -73.10004773611281, 5.5082111783412156e-05, 0.8039381825557192, 7.711049919579462, 0.0691839256782161, 0.09262313050876601, 0.0012446636859846194, 0.0144001999144337, 0.0017700311104057842, 0.000592914432028037, -17.173900607231808, 3.314098938077324e-06, 0.012119913514216233]
        self.set_model_params(self.param_values)

class TC2(TC):
    def __init__(self):
        super(TC2, self).__init__(cell_id=2)
        self.param_values = [3.785462900582912, 89.79669396764854, 0.31585659822626116, 28.19785323159065, -74.04624816495644, -56.38714258327616, 1.3397520148020146e-05, 1.266312157656397, 1.8960864468662297, 0.09576266749957624, 0.09566232884798592, 0.000779451515046998, 0.00038116587823681876, 0.011087998364345571, 0.0005841114725223401, -12.314536976560017, 4.686157413175496e-08, 0.0021843751013996405]
        self.set_model_params(self.param_values)

class TC3(TC):
    def __init__(self):
        super(TC3, self).__init__(cell_id=3)
        self.param_values =  [1.293216812216099, 78.29710551944315, 2.097406597258892, 34.055225274390374, -63.05622789535423, -70.37583997122185, 0.0001864035484138474, 0.1829079577831676, 5.569533491055797, 0.09254844216346347, 0.09783738480668593, 0.0019712397105499805, 0.013421498472456014, 0.0012600446757832437, 0.0006439371677005635, -31.89161678401573, 5.567862768115105e-06, 0.014360324837566624]
        self.set_model_params(self.param_values)

class TC4(TC):
    def __init__(self):
        super(TC4, self).__init__(cell_id=4)
        self.param_values = [3.6612680027841957, 7.513990634502036, 0.33141621517079123, 31.550232972799943, -70.79505936496551, -66.65287317539591, 2.0582546231510253e-05, 1.68190400884515, 126.81440056198939, 0.08718891479433064, 0.08295348895553578, 0.000996649658869783, 0.005171758191340916, 0.0012604178722584979, 0.0001245895463527829, -33.73920805589267, 2.128468299481898e-06, 0.000293758972864559]
        self.set_model_params(self.param_values)

class TC5(TC):
    def __init__(self):
        super(TC5, self).__init__(cell_id=5)
        self.param_values = [4.446937462907198, 108.16943142285014, 0.5109605895198407, 27.398380694368175, -64.81862254095378, -71.4178034970298, 1.0976948190363097e-05, 1.5198045615935931, 15.841855189812122, 0.06117221685247211, 0.04401990455783584, 0.001653549911846703, 0.014675079343878576, 0.006512210027167893, 0.0002634651766067278, -24.322850063975935, 4.842492455784204e-09, 0.0007164470605316754]
        self.set_model_params(self.param_values)