# ex: set ro:
# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : AppClass.sm

import statemap


class AppClassState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def EOS(self, fsm):
        self.Default(fsm)

    def digit(self, fsm, c):
        self.Default(fsm)

    def equal(self, fsm):
        self.Default(fsm)

    def letter(self, fsm, c):
        self.Default(fsm)

    def operation(self, fsm):
        self.Default(fsm)

    def space(self, fsm):
        self.Default(fsm)

    def start(self, fsm):
        self.Default(fsm)

    def unknown(self, fsm):
        self.Default(fsm)

    def Default(self, fsm):
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException(msg)

class MainMap_Default(AppClassState):

    def start(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.ClearSMC()
        finally:
            fsm.setState(MainMap.Start)
            fsm.getState().Entry(fsm)


    def letter(self, fsm, c):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def digit(self, fsm, c):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def space(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def equal(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def unknown(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def operation(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


class MainMap_Start(MainMap_Default):

    def letter(self, fsm, c):
        ctxt = fsm.getOwner()
        if  ctxt.is_valid_type()  :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.counter_inc()
                ctxt.add_to_type_string(c)
            finally:
                fsm.setState(endState)
        else:
            MainMap_Default.letter(self, fsm, c)
        
    def space(self, fsm):
        ctxt = fsm.getOwner()
        if  ctxt.check_type()  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.counter_zero()
            finally:
                fsm.setState(MainMap.Space)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.space(self, fsm)
        
class MainMap_Space(MainMap_Default):

    def letter(self, fsm, c):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.counter_inc()
            ctxt.add_to_name_string(c)
        finally:
            fsm.setState(MainMap.LitName)
            fsm.getState().Entry(fsm)


class MainMap_LitName(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        if  ctxt.check_lit_flag_true() and ctxt.check_vocab() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Acceptable()
                ctxt.add_to_vocab()
            finally:
                fsm.setState(MainMap.OK)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.EOS(self, fsm)
        
    def digit(self, fsm, c):
        ctxt = fsm.getOwner()
        if  ctxt.is_valid_name()  :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.counter_inc()
                ctxt.add_to_name_string(c)
            finally:
                fsm.setState(endState)
        else:
            MainMap_Default.digit(self, fsm, c)
        
    def equal(self, fsm):
        ctxt = fsm.getOwner()
        if  ctxt.check_lit_flag_false() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.set_lit_flag()
                ctxt.counter_zero()
            finally:
                fsm.setState(MainMap.EqOp)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.equal(self, fsm)
        
    def letter(self, fsm, c):
        ctxt = fsm.getOwner()
        if  ctxt.is_valid_name()  :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.counter_inc()
                ctxt.add_to_name_string(c)
            finally:
                fsm.setState(endState)
        else:
            MainMap_Default.letter(self, fsm, c)
        
    def operation(self, fsm):
        ctxt = fsm.getOwner()
        if  ctxt.check_lit_flag_true() and ctxt.check_op_flag_false() and ctxt.check_vocab() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.set_op_flag()
                ctxt.counter_zero()
                ctxt.clear_tmp_name_string()
            finally:
                fsm.setState(MainMap.EqOp)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.operation(self, fsm)
        
class MainMap_EqOp(MainMap_Default):

    def digit(self, fsm, c):
        fsm.getState().Exit(fsm)
        fsm.setState(MainMap.LitDig)
        fsm.getState().Entry(fsm)


    def letter(self, fsm, c):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.counter_inc()
            ctxt.add_to_name_string(c)
        finally:
            fsm.setState(MainMap.LitName)
            fsm.getState().Entry(fsm)


class MainMap_LitDig(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Acceptable()
            ctxt.add_to_vocab()
        finally:
            fsm.setState(MainMap.OK)
            fsm.getState().Entry(fsm)


    def digit(self, fsm, c):
        fsm.getState().Exit(fsm)
        fsm.setState(MainMap.LitDig)
        fsm.getState().Entry(fsm)


    def operation(self, fsm):
        ctxt = fsm.getOwner()
        if  ctxt.check_op_flag_false() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.set_op_flag()
            finally:
                fsm.setState(MainMap.EqOp)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.operation(self, fsm)
        
class MainMap_OK(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.Acceptable()
        finally:
            fsm.setState(endState)


class MainMap_Error(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(endState)


class MainMap(object):

    Start = MainMap_Start('MainMap.Start', 0)
    Space = MainMap_Space('MainMap.Space', 1)
    LitName = MainMap_LitName('MainMap.LitName', 2)
    EqOp = MainMap_EqOp('MainMap.EqOp', 3)
    LitDig = MainMap_LitDig('MainMap.LitDig', 4)
    OK = MainMap_OK('MainMap.OK', 5)
    Error = MainMap_Error('MainMap.Error', 6)
    Default = MainMap_Default('MainMap.Default', -1)

class AppClass_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self, MainMap.Start)
        self._owner = owner

    def __getattr__(self, attrib):
        def trans_sm(*arglist):
            self._transition = attrib
            getattr(self.getState(), attrib)(self, *arglist)
            self._transition = None
        return trans_sm

    def enterStartState(self):
        self._state.Entry(self)

    def getOwner(self):
        return self._owner

# Local variables:
#  buffer-read-only: t
# End:
