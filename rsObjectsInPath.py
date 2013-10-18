# rsObjectsInPath
# @author Roberto Rubio
# @date 2013-10-17
# @file rsObjectsInPath.py

import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.cmds as cmds

kPluginCmdRsObjectsInPathUI = "rsObjectsInPathUI"


##
# rs Objects in Path UI launch class.
# launch UI for objects in path.
class rsObjectsInPathUIClass(OpenMayaMPx.MPxCommand):

    ##
    # rsObjectsInPathUI Constructor.
    # @param self: Object pointer.
    # @return none
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

    ##
    # Do it function.
    # @param self: Object pointer.
    # @param argList: Command arguments.
    # @return none
    def doIt(self, argList):
        rsObjecsInPathUI()


##
# Creating instance event.
# @param none.
# @return cmdCreatorrsObjectsInPathUI instance
def cmdCreatorrsObjectsInPathUI():
    return OpenMayaMPx.asMPxPtr(rsObjectsInPathUIClass())


kPluginCmdRsObjectsInPath = "rsObjectsInPathCmd"

kNumberFlag = "-n"
kNumberLongFlag = "-i_number"
kTypeFlag = "-t"
kTypeLongFlag = "-i_type"
kPosFlag = "-cp"
kPosLongFlag = "-b_consPos"
kOriFlag = "-co"
kOriLongFlag = "-b_consOri"
kWorldFlag = "-wo"
kWorldLongFlag = "-b_orientWorld"
kParentFlag = "-p"
kParentLongFlag = "-b_parentHierarchy"
kSelectFlag = "-s"
kSelectLongFlag = "-b_selectNewObjs"
kObjectFlag = "-o"
kObjectLongFlag = "-o_toCurve"
kInstanceFlag = "-i"
kInstanceLongFlag = "-i_instance"
kLoftFlag = "-l"
kLoftLongFlag = "-i_loft"


##
# rs Objects in Path command class.
# Launch command for substitute Attributes.
class rsObjectsInPathCmdClass(OpenMayaMPx.MPxCommand):

    ##
    # rsObjectsInPathCmd Constructor.
    # @param self: Object pointer.
    # @return none
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

    ##
    # Do it function.
    # @param self: Object pointer.
    # @param argList: Command arguments.
    # @return none
    def doIt(self, argList):
        b_flag = False
        try:
            argData = OpenMaya.MArgDatabase(self.syntax(), argList)
            b_flag = True
        except:
            print("Invalid Arguments")
            pass
        if b_flag:
            sList = OpenMaya.MSelectionList()
            argData.getObjects(sList)
            l_curves = []
            if sList.length() != 0:
                sList.getSelectionStrings(l_curves)
            if argData.isFlagSet(kNumberFlag):
                i_number = argData.flagArgumentInt(kNumberFlag, 0)
            else:
                i_number = 3
            if argData.isFlagSet(kTypeFlag):
                i_type = argData.flagArgumentInt(kTypeFlag, 0)
            else:
                i_type = 0
            if argData.isFlagSet(kPosFlag):
                b_consPos = argData.flagArgumentBool(kPosFlag, 0)
            else:
                b_consPos = True
            if argData.isFlagSet(kOriFlag):
                b_consOri = argData.flagArgumentBool(kOriFlag, 0)
            else:
                b_consOri = True
            if argData.isFlagSet(kWorldFlag):
                b_orientWorld = argData.flagArgumentBool(kWorldFlag, 0)
            else:
                b_orientWorld = False
            if argData.isFlagSet(kParentFlag):
                b_parentHierarchy = argData.flagArgumentBool(kParentFlag, 0)
            else:
                b_parentHierarchy = False
            if argData.isFlagSet(kSelectFlag):
                b_selectNewObjs = argData.flagArgumentBool(kSelectFlag, 0)
            else:
                b_selectNewObjs = True
            if argData.isFlagSet(kObjectFlag):
                o_toCurve = argData.flagArgumentString(kObjectFlag, 0)
            else:
                o_toCurve = None
            if argData.isFlagSet(kInstanceFlag):
                i_instance = argData.flagArgumentInt(kInstanceFlag, 0)
            else:
                i_instance = 0
            if argData.isFlagSet(kLoftFlag):
                i_loft = argData.flagArgumentInt(kLoftFlag, 0)
            else:
                i_loft = 0
            if sList.length() > 0:
                l_objsInPath = rsObjectsInPath(l_curves, i_number, i_type, b_consPos, b_consOri, b_orientWorld, b_parentHierarchy, b_selectNewObjs, o_toCurve, i_instance, i_loft)
            else:
                raise RuntimeError("You need at least one object")
            return l_objsInPath


##
# Creating instance event.
# @param none.
# @return rsObjectsInPathCmd instance
def cmdCreatorrsObjectsInPath():
    return OpenMayaMPx.asMPxPtr(rsObjectsInPathCmdClass())


# Objects in path arguments creator event.
# @param none.
# @return syntax instance
def syntaxCreatorRsObjectsInPath():
    syntax = OpenMaya.MSyntax()
    syntax.addFlag(kNumberFlag, kNumberLongFlag, OpenMaya.MSyntax.kLong)
    syntax.addFlag(kTypeFlag, kTypeLongFlag, OpenMaya.MSyntax.kLong)
    syntax.addFlag(kPosFlag, kPosLongFlag, OpenMaya.MSyntax.kBoolean)
    syntax.addFlag(kOriFlag, kOriLongFlag, OpenMaya.MSyntax.kBoolean)
    syntax.addFlag(kWorldFlag, kWorldLongFlag, OpenMaya.MSyntax.kBoolean)
    syntax.addFlag(kParentFlag, kParentLongFlag, OpenMaya.MSyntax.kBoolean)
    syntax.addFlag(kSelectFlag, kSelectLongFlag, OpenMaya.MSyntax.kBoolean)
    syntax.addFlag(kObjectFlag, kObjectLongFlag, OpenMaya.MSyntax.kString)
    syntax.addFlag(kInstanceFlag, kInstanceLongFlag, OpenMaya.MSyntax.kLong)
    syntax.addFlag(kLoftFlag, kLoftLongFlag, OpenMaya.MSyntax.kLong)
    syntax.useSelectionAsDefault(True)
    syntax.setObjectType(OpenMaya.MSyntax.kSelectionList)
    return syntax


##
# Load Plugin event.
# @param obj.
# @return none
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject, 'Rig Studio - Developer: Roberto Rubio', '1.0', 'Any')
    try:
        mplugin.registerCommand(kPluginCmdRsObjectsInPathUI, cmdCreatorrsObjectsInPathUI)
        mplugin.registerCommand(kPluginCmdRsObjectsInPath, cmdCreatorrsObjectsInPath, syntaxCreatorRsObjectsInPath)
        mplugin.addMenuItem("rs Objects In Path", "MayaWindow|mainConstraintsMenu", "rsObjectsInPathUI()", "")
        mplugin.addMenuItem("rs Objects In Path", "MayaWindow|mainKeysMenu", "rsObjectsInPathUI()", "")
    except:
        raise RuntimeError("Failed to register command: %s\ n" % kPluginCmdRsObjectsInPathUI)
        raise RuntimeError("Failed to register command: %s\ n" % kPluginCmdRsObjectsInPath)


##
# Unload Plugin event.
# @param obj.
# @return none
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(kPluginCmdRsObjectsInPathUI)
        mplugin.deregisterCommand(kPluginCmdRsObjectsInPath)
        cmds.deleteUI("MayaWindow|mainConstraintsMenu|rs_Objects_In_Path")
        cmds.deleteUI("MayaWindow|mainKeysMenu|rs_Objects_In_Path")
    except:
        raise RuntimeError("Failed to unregister command: %s\n" % kPluginCmdRsObjectsInPathUI)
        raise RuntimeError("Failed to unregister command: %s\n" % kPluginCmdRsObjectsInPath)


##
# rs Objects in path UI class.
# Create UI for objects in path.
class rsObjecsInPathUI():

    ##
    # UI Constructor.
    # @param self: Object pointer.
    # @return none
    def __init__(self):
        self.name = "rsObjectsInPathUI"
        self.title = "rs Objects In Path"
        i_windowSize = (300, 385)
        if (cmds.window(self.name, q=1, exists=1)):
            cmds.deleteUI(self.name)
        self.window = cmds.window(self.name, title=self.title)
        s_winColPro2 = cmds.columnLayout(adjustableColumn=True, parent=self.window)
        s_winLayOr = cmds.frameLayout(label='Constrain objects in path', li=70, borderStyle='etchedOut', height=140, parent=s_winColPro2)
        s_winColA = cmds.columnLayout(adjustableColumn=True, parent=s_winLayOr)
        cmds.separator(height=10, style="none", hr=True, parent=s_winColA)
        self.intSliderObInPa = cmds.intSliderGrp(field=True, label='Objects in Path', cal=(1, "center"), cw=[(1, 90), (2, 50), (3, 100)], ad3=3, minValue=3, maxValue=50, fieldMinValue=3, fieldMaxValue=1000, value=3, parent=s_winColA)
        cmds.separator(height=10, style="none", hr=True, parent=s_winColA)
        cmds.rowLayout(numberOfColumns=6, cw=[(1, 2), (2, 90), (3, 2), (4, 90), (5, 5), (6, 110)], parent=s_winColA)
        cmds.separator(height=10, style="none", hr=True, parent=s_winColA)
        s_winLayOptions = cmds.frameLayout(lv=False, borderStyle='in', parent=s_winColA)
        s_winLayOptionsCol = cmds.columnLayout(adjustableColumn=True, parent=s_winLayOptions)
        cmds.separator(height=5, style="none", hr=True, parent=s_winLayOptionsCol)
        s_winRowA = cmds.rowLayout(numberOfColumns=6, cw=[(1, 2), (2, 90), (3, 2), (4, 90), (5, 5), (6, 110)], parent=s_winLayOptionsCol)
        cmds.separator(height=5, style="none", hr=True, parent=s_winRowA)
        self.mainPosObInPa = cmds.checkBox("rsConsPos", label='Cons Position', cc=self.rsMaintPos, align='right', v=True, parent=s_winRowA)
        cmds.separator(height=5, style="none", hr=True, parent=s_winRowA)
        self.mainTangObInPa = cmds.checkBox("rsConsOri", label='Cons Rotation', cc=self.rsMaintTan, align='right', v=True, parent=s_winRowA)
        cmds.separator(height=5, style="none", hr=True, parent=s_winRowA)
        cmds.separator(height=10, style="none", hr=True, parent=s_winLayOptionsCol)
        self.globalOriObInPaObInPa = cmds.checkBox("rsglobalOriObInPaentation", label='Global Rotation', align='right', v=False, en=False, parent=s_winRowA)
        s_winRowB = cmds.rowLayout(numberOfColumns=4, cw=[(1, 20), (2, 110), (3, 20), (4, 90)], parent=s_winLayOptionsCol)
        cmds.separator(height=5, style="none", hr=True, parent=s_winRowB)
        self.parentHierarObInPa = cmds.checkBox("rsParentHierarchyObInPa", label='Parent Hierarchy', align='right', v=False, parent=s_winRowB, en=False)
        cmds.separator(height=5, style="none", hr=True, parent=s_winRowB)
        self.selectNewObjsObInPa = cmds.checkBox("rsSelectNewObjsObInPa", label='Select New Objects', align='right', v=True, parent=s_winRowB)
        cmds.separator(height=5, style="none", hr=True, parent=s_winLayOptions)
        cmds.separator(height=10, style="none", hr=True, parent=s_winColA)
        s_winLayObjects = cmds.frameLayout(label='Objects for the path', li=86, borderStyle='etchedOut', parent=s_winColPro2)
        s_winColB = cmds.columnLayout(adjustableColumn=True, parent=s_winLayObjects)
        cmds.separator(height=10, style="none", hr=True, parent=s_winColB)
        s_winRowType = cmds.rowLayout(numberOfColumns=2, adjustableColumn3=2, cw=[(1, 4), (2, 100)], parent=s_winColB)
        cmds.separator(width=4, style="none", hr=True, parent=s_winRowType)
        self.opMenuCoInPa = cmds.attrEnumOptionMenu(l='Object type   ',
                            ei=[(0, '    Empty Group'), (1, '    Locator'), (2, '    Joint'), (3, '    Scene Object     ')], cc=self.rsObjTypeCoInPa, parent=s_winRowType)
        cmds.separator(height=10, style="none", hr=True, parent=s_winColB)
        s_winLayObjOptions = cmds.frameLayout(lv=False, borderStyle='in', parent=s_winColB)
        s_winLayObjOptionsCol = cmds.columnLayout(adjustableColumn=True, parent=s_winLayObjOptions)
        cmds.separator(height=10, style="none", hr=True, parent=s_winLayObjOptionsCol)
        s_winRowObjects = cmds.rowLayout(numberOfColumns=3, adjustableColumn3=2, cw=[(1, 70), (2, 100), (3, 50)], columnAlign=(1, 'center'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)], parent=s_winLayObjOptionsCol)
        self.textObInPa = cmds.text(label='Scene object', align='center', parent=s_winRowObjects, en=False)
        self.fieldObInPa = cmds.textField(cmds.textField(), cc=self.rsFieldObInPa, edit=True, parent=s_winRowObjects, text=None, en=False)
        self.buttonObInPa = cmds.button(label='Pick up', c=self.rsPickObInPa, parent=s_winRowObjects, en=False)
        cmds.separator(height=10, style="none", hr=True, parent=s_winLayObjOptionsCol)
        s_winRowObjectsOptions = cmds.rowLayout(numberOfColumns=4, cw=[(1, 60), (2, 60), (3, 30), (4, 60)], columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0), (4, 'both', 0)], parent=s_winLayObjOptionsCol)
        cmds.separator(width=40, style="none", hr=True, parent=s_winRowObjectsOptions)
        cmds.radioCollection("OptionObject", parent=s_winRowObjectsOptions)
        self.copyObInPa = cmds.radioButton(label='Copy', parent=s_winRowObjectsOptions, en=False)
        cmds.separator(width=40, style="none", hr=True, parent=s_winRowObjectsOptions)
        self.instanceObInPa = cmds.radioButton(label='Instance', parent=s_winRowObjectsOptions, en=False)
        cmds.separator(height=10, style="none", hr=True, parent=s_winLayObjOptionsCol)
        self.frameLayoutLoftObInPa = cmds.frameLayout(label='Loft', li=128, lv=True, borderStyle='in', parent=s_winLayObjOptionsCol, en=False)
        s_winLayLoftButtonsCol = cmds.columnLayout(adjustableColumn=True, parent=self.frameLayoutLoftObInPa)
        cmds.separator(height=5, style="none", hr=True, parent=s_winLayLoftButtonsCol)
        s_winLayObjOptCurveOps = cmds.rowLayout(numberOfColumns=6, cw=[(1, 30), (2, 55), (3, 20), (4, 60), (5, 20), (6, 60)], columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0), (4, 'both', 0)], parent=s_winLayLoftButtonsCol)
        cmds.separator(width=10, style="none", hr=True, parent=s_winLayObjOptCurveOps)
        cmds.radioCollection("LoftOptions", parent=s_winLayObjOptCurveOps)
        self.opNoneObInPa = cmds.radioButton(label='None', parent=s_winLayObjOptCurveOps, en=False)
        cmds.separator(width=10, style="none", hr=True, parent=s_winLayObjOptCurveOps)
        self.opPolyObInPa = cmds.radioButton(label='Poligons', parent=s_winLayObjOptCurveOps, en=False)
        cmds.separator(width=10, style="none", hr=True, parent=s_winLayObjOptCurveOps)
        self.opNurbsObInPa = cmds.radioButton(label='Nurbs', parent=s_winLayObjOptCurveOps, en=False)
        cmds.separator(height=5, style="none", hr=True, parent=s_winLayLoftButtonsCol)
        cmds.separator(height=10, style="none", hr=True, parent=s_winColPro2)
        self.rsLaunchObInPa = cmds.button(label='Execute', w=100, c=self.rsLaunchObInPa, parent=s_winColPro2)
        self.rsTextObInPa = cmds.text(label='    Empty Group', vis=False, parent=s_winColPro2)
        cmds.window(self.window, e=1, w=430, h=103)
        cmds.showWindow(self.window)
        cmds.radioButton(self.instanceObInPa, e=True, select=True)
        cmds.radioButton(self.opNoneObInPa, e=True, select=True)
        cmds.window(self.window, edit=True, widthHeight=(i_windowSize), s=False)

    ##
    # rsMaintTan function.
    # @param self: Object pointer.
    # @param argList: Command arguments.
    # @return none
    def rsMaintTan(self, *args):
        if cmds.checkBox(self.globalOriObInPaObInPa, q=True, en=True) == False:
            cmds.checkBox(self.globalOriObInPaObInPa, e=True, en=True)
        else:
            cmds.checkBox(self.globalOriObInPaObInPa, e=True, v=False)
            cmds.checkBox(self.globalOriObInPaObInPa, e=True, en=False)
        if cmds.checkBox(self.mainPosObInPa, q=True, v=True) == False and cmds.checkBox(self.mainTangObInPa, q=True, v=True) == False:
            cmds.checkBox(self.parentHierarObInPa, e=True, en=True)
        else:
            cmds.checkBox(self.parentHierarObInPa, e=True, v=False)
            cmds.checkBox(self.parentHierarObInPa, e=True, en=False)

    ##
    # rsMaintPos function.
    # @param self: Object pointer.
    # @param argList: Command arguments.
    # @return none
    def rsMaintPos(self, *args):
        if cmds.checkBox(self.mainPosObInPa, q=True, v=True) == False and cmds.checkBox(self.mainTangObInPa, q=True, v=True) == False:
            cmds.checkBox(self.parentHierarObInPa, e=True, en=True)
        else:
            cmds.checkBox(self.parentHierarObInPa, e=True, v=False)
            cmds.checkBox(self.parentHierarObInPa, e=True, en=False)

    ##
    # rsObjTypeCoInPa function.
    # @param self: Object pointer.
    # @param argList: Command arguments.
    # @return none
    def rsObjTypeCoInPa(self, *args):
        cmds.text(self.rsTextObInPa, e=True, l=args[0])
        if args[0] == '    Scene Object     ':
            cmds.text(self.textObInPa, e=True, en=True)
            cmds.textField(self.fieldObInPa, e=True, en=True)
            cmds.button(self.buttonObInPa, e=True, en=True)
            cmds.radioButton(self.copyObInPa, e=True, en=True)
            cmds.radioButton(self.instanceObInPa, e=True, en=True)
        else:
            cmds.text(self.textObInPa, e=True, en=False)
            cmds.textField(self.fieldObInPa, e=True, text=None)
            cmds.textField(self.fieldObInPa, e=True, en=False)
            cmds.button(self.buttonObInPa, e=True, en=False)
            cmds.radioButton(self.copyObInPa, e=True, en=False)
            cmds.radioButton(self.instanceObInPa, e=True, en=False)
            cmds.radioButton(self.opNoneObInPa, e=True, select=True)
            cmds.frameLayout(self.frameLayoutLoftObInPa, e=True, en=False)
            cmds.radioButton(self.opNoneObInPa, e=True, en=False)
            cmds.radioButton(self.opPolyObInPa, e=True, en=False)
            cmds.radioButton(self.opNurbsObInPa, e=True, en=False)

    ##
    # rsPickObInPa function.
    # @param self: Object pointer.
    # @param argList: Command arguments.
    # @return none
    def rsPickObInPa(self, *args):
        sel = cmds.ls(sl=True, o=False)
        if len(sel) > 0:
            if len(sel) > 1:
                cmds.warning("Too many object selecteds")
            cmds.textField(self.fieldObInPa, e=True, text=sel[0])
            o_shape = cmds.listRelatives(sel[0], s=True)[0]
            if cmds.nodeType(o_shape) == "nurbsCurve" or cmds.nodeType(o_shape) == "bezierCurve":
                cmds.frameLayout(self.frameLayoutLoftObInPa, e=True, en=True)
                cmds.radioButton(self.opNoneObInPa, e=True, en=True)
                cmds.radioButton(self.opPolyObInPa, e=True, en=True)
                cmds.radioButton(self.opNurbsObInPa, e=True, en=True)
            else:
                cmds.radioButton(self.opNoneObInPa, e=True, select=True)
                cmds.frameLayout(self.frameLayoutLoftObInPa, e=True, en=False)
                cmds.radioButton(self.opNoneObInPa, e=True, en=False)
                cmds.radioButton(self.opPolyObInPa, e=True, en=False)
                cmds.radioButton(self.opNurbsObInPa, e=True, en=False)
        else:
            cmds.warning("Select an object, please")
            cmds.textField(self.fieldObInPa, e=True, text="")

    ##
    # rsFieldObInPa function.
    # @param self: Object pointer.
    # @param argList: Command arguments.
    # @return none
    def rsFieldObInPa(self, *args):
        o_sceneObj = cmds.textField(self.fieldObInPa, q=True, text=True)
        if cmds.objExists(o_sceneObj):
            o_shape = cmds.listRelatives(o_sceneObj, s=True)[0]
            if cmds.nodeType(o_shape) == "nurbsCurve" or cmds.nodeType(o_shape) == "bezierCurve":
                cmds.frameLayout(self.frameLayoutLoftObInPa, e=True, en=True)
                cmds.radioButton(self.opNoneObInPa, e=True, en=True)
                cmds.radioButton(self.opPolyObInPa, e=True, en=True)
                cmds.radioButton(self.opNurbsObInPa, e=True, en=True)
            else:
                cmds.radioButton(self.opNoneObInPa, e=True, select=True)
                cmds.frameLayout(self.frameLayoutLoftObInPa, e=True, en=False)
                cmds.radioButton(self.opNoneObInPa, e=True, en=False)
                cmds.radioButton(self.opPolyObInPa, e=True, en=False)
                cmds.radioButton(self.opNurbsObInPa, e=True, en=False)
        else:
            cmds.warning("Wrong input argument")
            cmds.textField(self.fieldObInPa, e=True, text="")
            cmds.radioButton(self.opNoneObInPa, e=True, select=True)
            cmds.frameLayout(self.frameLayoutLoftObInPa, e=True, en=False)
            cmds.radioButton(self.opNoneObInPa, e=True, en=False)
            cmds.radioButton(self.opPolyObInPa, e=True, en=False)
            cmds.radioButton(self.opNurbsObInPa, e=True, en=False)

    ##
    # rsLaunchObInPa function.
    # @param self: Object pointer.
    # @param argList: Command arguments.
    # @return none
    def rsLaunchObInPa(self, *args):
        d_type = {'    Empty Group': 0, '    Locator': 1, '    Joint': 2, '    Scene Object     ': 3}
        l_curves = cmds.ls(selection=True)
        i_number = cmds.intSliderGrp(self.intSliderObInPa, q=True, v=True)
        s_type = cmds.text(self.rsTextObInPa, q=True, l=True)
        i_type = d_type[s_type]
        b_consPos = cmds.checkBox(self.mainPosObInPa, q=True, v=True)
        b_consOri = cmds.checkBox(self.mainTangObInPa, q=True, v=True)
        b_orientWorld = cmds.checkBox(self.globalOriObInPaObInPa, q=True, v=True)
        b_parentHierarchy = cmds.checkBox(self.parentHierarObInPa, q=True, v=True)
        b_selectNewObjs = cmds.checkBox(self.selectNewObjsObInPa, q=True, v=True)
        o_toCurve = cmds.textField(self.fieldObInPa, q=True, text=True)
        if o_toCurve == "":
            o_toCurve = None
        try:
            if cmds.objExists(o_toCurve):
                pass
        except:
            o_toCurve = None
        i_instance = cmds.radioButton(self.instanceObInPa, q=True, select=True)
        i_loft = 0
        if cmds.radioButton(self.opPolyObInPa, q=True, select=True):
            i_loft = 1
        if cmds.radioButton(self.opNurbsObInPa, q=True, select=True):
            i_loft = 2
        rsObjectsInPath(l_curves, i_number, i_type, b_consPos, b_consOri, b_orientWorld, b_parentHierarchy, b_selectNewObjs, o_toCurve, i_instance, i_loft)
        #rsObjectsInPath(l_curves, i_number,i_type, b_consPos, b_consOri, b_orientWorld, o_toCurve, i_instance)


##
# rs Objects in path function..
# @param l_curves - paths list.
# @param i_number - integer. Number objects to path.
# @param i_type - integer. Type objects to path.
# @param b_consPos - Boolean. Defines whether objects have position constraint.
# @param b_consOri - Boolean. Defines whether objects have orientation constraint.
# @param b_orientWorld - Boolean. Defines whether objects have global orientation.
# @param b_parentHierarchy - Boolean. Defines whether objects will be related.
# @param b_selectNewObjs - Boolean. Defines whether objects will be selected.
# @param o_toCurve - String. Scene object to duplicate in path.
# @param i_instance - Integer. Defines whether o_toCurve will be instantiated.
# @param i_loft - Integer. Defines whether loft will be created and what type.
# @return l_objReturns - objects generated list.
# @return l_targets - Curve shapes list.
def rsObjectsInPath(l_curves, i_number=3, i_type=0, b_consPos=True, b_consOri=True, b_orientWorld=True, b_parentHierarchy=False, b_selectNewObjs=True, o_toCurve=None, i_instance=0, i_loft=0):
    l_selIn = cmds.ls(sl=True, o=False)
    cmds.select(cl=True)
    l_list = []
    try:
        if cmds.objExists(l_curves):
            l_list.append(l_curves)
    except:
        pass
    for o_obj in l_curves:
        if cmds.objExists(o_obj):
            l_list.append(o_obj)
    if len(l_list) == 0:
        cmds.warning("Wrong input argument")
        return False
    l_curves = l_list
    d_type = {0: "group", 1: "spaceLocator", 2: "joint", 3: "Scene object"}
    l_targets = []
    l_objReturns = []
    for o_obj in l_curves:
        if cmds.objExists(o_obj):
            l_shapes = cmds.listRelatives(o_obj, s=True)
            for o_shape in l_shapes:
                if cmds.nodeType(o_shape) == "nurbsCurve" or cmds.nodeType(o_shape) == "bezierCurve":
                    l_targets.append(o_shape)
        else:
            cmds.warning("%s > A Does not exist" % (o_obj))
    if len(l_targets) > 0:
        l_loft = []
        for o_target in l_targets:
            l_tmpObjReturns = []
            i_openCloseVal = cmds.getAttr("%s.f" % (o_target))
            if i_openCloseVal == 0:
                f_div = 1.00 / (i_number - 1)
            else:
                f_div = 1.00 / i_number
            l_uValues = []
            for z in range(i_number):
                l_uValues.append(f_div * z)
            for z in range(i_number):
                o_obj = None
                if i_type != 3:
                    if i_type in d_type:
                        if i_type == 0:
                            o_obj = cmds.group(em=True)
                        if i_type == 1:
                            o_obj = cmds.spaceLocator()[0]
                        if i_type == 2:
                            o_obj = cmds.joint()
                    else:
                        cmds.warning("Type not recognized")
                        break
                else:
                    if cmds.objExists(o_toCurve):
                        if i_instance == 0:
                            o_obj = cmds.duplicate(o_toCurve)[0]
                        else:
                            o_obj = cmds.instance(o_toCurve)[0]
                    else:
                        cmds.warning("%s > B Does not exist" % (o_toCurve))
                        break
                l_objReturns.append(o_obj)
                l_tmpObjReturns.append(o_obj)
                o_path = cmds.pathAnimation(o_obj, o_target, f=b_consOri, fractionMode=True, followAxis="y", upAxis="z", worldUpType="vector")
                o_incomingConnection = cmds.listConnections("%s.uValue" % (o_path), destination=False, source=True)[0]
                cmds.cycleCheck(e=0)
                cmds.delete(o_incomingConnection)
                cmds.cycleCheck(e=1)
                cmds.setAttr("%s.uValue" % (o_path), l_uValues[z])
                if not b_consOri and not b_consPos:
                    o_incoming = cmds.listConnections("%s.rotateX" % (o_obj), destination=False, source=True)[0]
                    cmds.cycleCheck(e=0)
                    cmds.delete(o_incoming)
                    cmds.cycleCheck(e=1)
                if b_consOri and not b_consPos:
                    o_incomingX = cmds.listConnections("%s.translateX" % (o_obj), plugs=True, destination=False, source=True)[0]
                    o_incomingY = cmds.listConnections("%s.translateY" % (o_obj), plugs=True, destination=False, source=True)[0]
                    o_incomingZ = cmds.listConnections("%s.translateZ" % (o_obj), plugs=True, destination=False, source=True)[0]
                    cmds.disconnectAttr(o_incomingX, "%s.translateX" % (o_obj))
                    cmds.disconnectAttr(o_incomingY, "%s.translateY" % (o_obj))
                    cmds.disconnectAttr(o_incomingZ, "%s.translateZ" % (o_obj))
                if not b_consOri and b_consPos:
                    o_incomingX = cmds.listConnections("%s.rotateX" % (o_obj), plugs=True, destination=False, source=True)[0]
                    o_incomingY = cmds.listConnections("%s.rotateY" % (o_obj), plugs=True, destination=False, source=True)[0]
                    o_incomingZ = cmds.listConnections("%s.rotateZ" % (o_obj), plugs=True, destination=False, source=True)[0]
                    cmds.disconnectAttr(o_incomingX, "%s.rotateX" % (o_obj))
                    cmds.disconnectAttr(o_incomingY, "%s.rotateY" % (o_obj))
                    cmds.disconnectAttr(o_incomingZ, "%s.rotateZ" % (o_obj))
                    cmds.setAttr("%s.follow" % (o_path), b_consOri)
                if not b_consOri and b_orientWorld:
                    cmds.setAttr("%s.rotateX" % (o_obj), 0)
                    cmds.setAttr("%s.rotateY" % (o_obj), 0)
                    cmds.setAttr("%s.rotateZ" % (o_obj), 0)
                cmds.select(cl=True)
            o_loft = ""
            if i_loft > 0:
                if i_loft == 1:
                    o_loftPoly = cmds.loft(l_tmpObjReturns, ch=1, u=1, c=0, ar=1, d=3, ss=1, rn=0, po=1, rsn=True)
                    o_outcoming = cmds.listConnections("%s.outputSurface" % (o_loftPoly[1]), plugs=False, destination=True, source=False)[0]
                    o_loft = o_loftPoly[1]
                    l_loft.append(o_loftPoly[0])
                    cmds.setAttr("%s.polygonType" % (o_outcoming), 1)
                    cmds.setAttr("%s.format" % (o_outcoming), 2)
                    cmds.setAttr("%s.uType" % (o_outcoming), 3)
                    cmds.setAttr("%s.uNumber" % (o_outcoming), 1)
                    cmds.setAttr("%s.vType" % (o_outcoming), 3)
                    cmds.setAttr("%s.vNumber" % (o_outcoming), 1)
                if i_loft == 2:
                    cmds.loft(l_tmpObjReturns, ch=1, u=1, c=0, ar=1, d=3, ss=1, rn=0, po=0, rsn=True)
                if i_loft > 2:
                    cmds.warning("Loft type not recognized")
            cmds.select(cl=True)
            if b_parentHierarchy:
                if not b_consPos and not b_consOri:
                    l_tmpObjReturns.reverse()
                    for z in range(len(l_tmpObjReturns) - 1):
                        cmds.parent(l_tmpObjReturns[z], l_tmpObjReturns[z + 1])
                else:
                    cmds.warning("Objects cannot be in hierarchy, , they have transformations constraints")
            cmds.select(cl=True)
        if b_selectNewObjs:
            if l_objReturns != []:
                cmds.select(l_objReturns)
                if len(l_loft) > 0:
                    cmds.select(l_loft, add=True)
            else:
                if l_selIn != []:
                    cmds.select(l_selIn)
        else:
            if l_selIn != []:
                cmds.select(l_selIn)
    return(l_objReturns, l_targets, l_loft)
