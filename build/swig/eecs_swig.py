# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_eecs_swig', [dirname(__file__)])
        except ImportError:
            import _eecs_swig
            return _eecs_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_eecs_swig', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _eecs_swig = swig_import_helper()
    del swig_import_helper
else:
    import _eecs_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    """Proxy of C++ swig::SwigPyIterator class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _eecs_swig.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self):
        """value(self) -> PyObject"""
        return _eecs_swig.SwigPyIterator_value(self)

    def incr(self, n = 1):
        """incr(self, size_t n = 1) -> SwigPyIterator"""
        return _eecs_swig.SwigPyIterator_incr(self, n)

    def decr(self, n = 1):
        """decr(self, size_t n = 1) -> SwigPyIterator"""
        return _eecs_swig.SwigPyIterator_decr(self, n)

    def distance(self, *args, **kwargs):
        """distance(self, SwigPyIterator x) -> ptrdiff_t"""
        return _eecs_swig.SwigPyIterator_distance(self, *args, **kwargs)

    def equal(self, *args, **kwargs):
        """equal(self, SwigPyIterator x) -> bool"""
        return _eecs_swig.SwigPyIterator_equal(self, *args, **kwargs)

    def copy(self):
        """copy(self) -> SwigPyIterator"""
        return _eecs_swig.SwigPyIterator_copy(self)

    def next(self):
        """next(self) -> PyObject"""
        return _eecs_swig.SwigPyIterator_next(self)

    def __next__(self):
        """__next__(self) -> PyObject"""
        return _eecs_swig.SwigPyIterator___next__(self)

    def previous(self):
        """previous(self) -> PyObject"""
        return _eecs_swig.SwigPyIterator_previous(self)

    def advance(self, *args, **kwargs):
        """advance(self, ptrdiff_t n) -> SwigPyIterator"""
        return _eecs_swig.SwigPyIterator_advance(self, *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        """__eq__(self, SwigPyIterator x) -> bool"""
        return _eecs_swig.SwigPyIterator___eq__(self, *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        """__ne__(self, SwigPyIterator x) -> bool"""
        return _eecs_swig.SwigPyIterator___ne__(self, *args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        """__iadd__(self, ptrdiff_t n) -> SwigPyIterator"""
        return _eecs_swig.SwigPyIterator___iadd__(self, *args, **kwargs)

    def __isub__(self, *args, **kwargs):
        """__isub__(self, ptrdiff_t n) -> SwigPyIterator"""
        return _eecs_swig.SwigPyIterator___isub__(self, *args, **kwargs)

    def __add__(self, *args, **kwargs):
        """__add__(self, ptrdiff_t n) -> SwigPyIterator"""
        return _eecs_swig.SwigPyIterator___add__(self, *args, **kwargs)

    def __sub__(self, *args):
        """
        __sub__(self, ptrdiff_t n) -> SwigPyIterator
        __sub__(self, SwigPyIterator x) -> ptrdiff_t
        """
        return _eecs_swig.SwigPyIterator___sub__(self, *args)

    def __iter__(self): return self
SwigPyIterator_swigregister = _eecs_swig.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class d_theta(object):
    """<+description of block+>"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    def make(*args, **kwargs):
        """
        make(double freq, double rSat, double thetaSat, double sampRate) -> sptr

        Return a shared_ptr to a new instance of eecs::d_theta.

        To avoid accidental use of raw pointers, eecs::d_theta's constructor is in a private implementation class. eecs::d_theta::make is the public interface for creating new instances.

        Params: (freq, rSat, thetaSat, sampRate)
        """
        return _eecs_swig.d_theta_make(*args, **kwargs)

    make = staticmethod(make)
    def freq(self):
        """
        freq(self) -> double

        Params: (NONE)
        """
        return _eecs_swig.d_theta_freq(self)

    def rSat(self):
        """
        rSat(self) -> double

        Params: (NONE)
        """
        return _eecs_swig.d_theta_rSat(self)

    def thetaSat(self):
        """
        thetaSat(self) -> double

        Params: (NONE)
        """
        return _eecs_swig.d_theta_thetaSat(self)

    def sampRate(self):
        """
        sampRate(self) -> double

        Params: (NONE)
        """
        return _eecs_swig.d_theta_sampRate(self)

    def set_freq(self, *args, **kwargs):
        """
        set_freq(self, double freq)

        Params: (freq)
        """
        return _eecs_swig.d_theta_set_freq(self, *args, **kwargs)

    def set_rSat(self, *args, **kwargs):
        """
        set_rSat(self, double rSat)

        Params: (rSat)
        """
        return _eecs_swig.d_theta_set_rSat(self, *args, **kwargs)

    def set_thetaSat(self, *args, **kwargs):
        """
        set_thetaSat(self, double thetaSat)

        Params: (thetaSat)
        """
        return _eecs_swig.d_theta_set_thetaSat(self, *args, **kwargs)

    def set_sampRate(self, *args, **kwargs):
        """
        set_sampRate(self, double sampRate)

        Params: (sampRate)
        """
        return _eecs_swig.d_theta_set_sampRate(self, *args, **kwargs)

    __swig_destroy__ = _eecs_swig.delete_d_theta
    __del__ = lambda self : None;
d_theta_swigregister = _eecs_swig.d_theta_swigregister
d_theta_swigregister(d_theta)

def d_theta_make(*args, **kwargs):
  """
    d_theta_make(double freq, double rSat, double thetaSat, double sampRate) -> sptr

    Return a shared_ptr to a new instance of eecs::d_theta.

    To avoid accidental use of raw pointers, eecs::d_theta's constructor is in a private implementation class. eecs::d_theta::make is the public interface for creating new instances.

    Params: (freq, rSat, thetaSat, sampRate)
    """
  return _eecs_swig.d_theta_make(*args, **kwargs)

class d_theta_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::eecs::d_theta)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> d_theta_sptr
        __init__(self, d_theta p) -> d_theta_sptr
        """
        this = _eecs_swig.new_d_theta_sptr(*args)
        try: self.this.append(this)
        except: self.this = this
    def __deref__(self):
        """__deref__(self) -> d_theta"""
        return _eecs_swig.d_theta_sptr___deref__(self)

    __swig_destroy__ = _eecs_swig.delete_d_theta_sptr
    __del__ = lambda self : None;
    def make(self, *args, **kwargs):
        """
        make(self, double freq, double rSat, double thetaSat, double sampRate) -> sptr

        Return a shared_ptr to a new instance of eecs::d_theta.

        To avoid accidental use of raw pointers, eecs::d_theta's constructor is in a private implementation class. eecs::d_theta::make is the public interface for creating new instances.

        Params: (freq, rSat, thetaSat, sampRate)
        """
        return _eecs_swig.d_theta_sptr_make(self, *args, **kwargs)

    def freq(self):
        """
        freq(self) -> double

        Params: (NONE)
        """
        return _eecs_swig.d_theta_sptr_freq(self)

    def rSat(self):
        """
        rSat(self) -> double

        Params: (NONE)
        """
        return _eecs_swig.d_theta_sptr_rSat(self)

    def thetaSat(self):
        """
        thetaSat(self) -> double

        Params: (NONE)
        """
        return _eecs_swig.d_theta_sptr_thetaSat(self)

    def sampRate(self):
        """
        sampRate(self) -> double

        Params: (NONE)
        """
        return _eecs_swig.d_theta_sptr_sampRate(self)

    def set_freq(self, *args, **kwargs):
        """
        set_freq(self, double freq)

        Params: (freq)
        """
        return _eecs_swig.d_theta_sptr_set_freq(self, *args, **kwargs)

    def set_rSat(self, *args, **kwargs):
        """
        set_rSat(self, double rSat)

        Params: (rSat)
        """
        return _eecs_swig.d_theta_sptr_set_rSat(self, *args, **kwargs)

    def set_thetaSat(self, *args, **kwargs):
        """
        set_thetaSat(self, double thetaSat)

        Params: (thetaSat)
        """
        return _eecs_swig.d_theta_sptr_set_thetaSat(self, *args, **kwargs)

    def set_sampRate(self, *args, **kwargs):
        """
        set_sampRate(self, double sampRate)

        Params: (sampRate)
        """
        return _eecs_swig.d_theta_sptr_set_sampRate(self, *args, **kwargs)

    def history(self):
        """history(self) -> unsigned int"""
        return _eecs_swig.d_theta_sptr_history(self)

    def output_multiple(self):
        """output_multiple(self) -> int"""
        return _eecs_swig.d_theta_sptr_output_multiple(self)

    def relative_rate(self):
        """relative_rate(self) -> double"""
        return _eecs_swig.d_theta_sptr_relative_rate(self)

    def start(self):
        """start(self) -> bool"""
        return _eecs_swig.d_theta_sptr_start(self)

    def stop(self):
        """stop(self) -> bool"""
        return _eecs_swig.d_theta_sptr_stop(self)

    def nitems_read(self, *args, **kwargs):
        """nitems_read(self, unsigned int which_input) -> uint64_t"""
        return _eecs_swig.d_theta_sptr_nitems_read(self, *args, **kwargs)

    def nitems_written(self, *args, **kwargs):
        """nitems_written(self, unsigned int which_output) -> uint64_t"""
        return _eecs_swig.d_theta_sptr_nitems_written(self, *args, **kwargs)

    def max_noutput_items(self):
        """max_noutput_items(self) -> int"""
        return _eecs_swig.d_theta_sptr_max_noutput_items(self)

    def set_max_noutput_items(self, *args, **kwargs):
        """set_max_noutput_items(self, int m)"""
        return _eecs_swig.d_theta_sptr_set_max_noutput_items(self, *args, **kwargs)

    def unset_max_noutput_items(self):
        """unset_max_noutput_items(self)"""
        return _eecs_swig.d_theta_sptr_unset_max_noutput_items(self)

    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(self) -> bool"""
        return _eecs_swig.d_theta_sptr_is_set_max_noutput_items(self)

    def max_output_buffer(self, *args, **kwargs):
        """max_output_buffer(self, int i) -> long"""
        return _eecs_swig.d_theta_sptr_max_output_buffer(self, *args, **kwargs)

    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(self, long max_output_buffer)
        set_max_output_buffer(self, int port, long max_output_buffer)
        """
        return _eecs_swig.d_theta_sptr_set_max_output_buffer(self, *args)

    def min_output_buffer(self, *args, **kwargs):
        """min_output_buffer(self, int i) -> long"""
        return _eecs_swig.d_theta_sptr_min_output_buffer(self, *args, **kwargs)

    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(self, long min_output_buffer)
        set_min_output_buffer(self, int port, long min_output_buffer)
        """
        return _eecs_swig.d_theta_sptr_set_min_output_buffer(self, *args)

    def pc_noutput_items(self):
        """pc_noutput_items(self) -> float"""
        return _eecs_swig.d_theta_sptr_pc_noutput_items(self)

    def pc_noutput_items_var(self):
        """pc_noutput_items_var(self) -> float"""
        return _eecs_swig.d_theta_sptr_pc_noutput_items_var(self)

    def pc_nproduced(self):
        """pc_nproduced(self) -> float"""
        return _eecs_swig.d_theta_sptr_pc_nproduced(self)

    def pc_nproduced_var(self):
        """pc_nproduced_var(self) -> float"""
        return _eecs_swig.d_theta_sptr_pc_nproduced_var(self)

    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(self, int which) -> float
        pc_input_buffers_full(self) -> __dummy_4__
        """
        return _eecs_swig.d_theta_sptr_pc_input_buffers_full(self, *args)

    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(self, int which) -> float
        pc_input_buffers_full_var(self) -> __dummy_4__
        """
        return _eecs_swig.d_theta_sptr_pc_input_buffers_full_var(self, *args)

    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(self, int which) -> float
        pc_output_buffers_full(self) -> __dummy_4__
        """
        return _eecs_swig.d_theta_sptr_pc_output_buffers_full(self, *args)

    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(self, int which) -> float
        pc_output_buffers_full_var(self) -> __dummy_4__
        """
        return _eecs_swig.d_theta_sptr_pc_output_buffers_full_var(self, *args)

    def pc_work_time(self):
        """pc_work_time(self) -> float"""
        return _eecs_swig.d_theta_sptr_pc_work_time(self)

    def pc_work_time_var(self):
        """pc_work_time_var(self) -> float"""
        return _eecs_swig.d_theta_sptr_pc_work_time_var(self)

    def set_processor_affinity(self, *args, **kwargs):
        """set_processor_affinity(self, gr_vector_uint mask)"""
        return _eecs_swig.d_theta_sptr_set_processor_affinity(self, *args, **kwargs)

    def unset_processor_affinity(self):
        """unset_processor_affinity(self)"""
        return _eecs_swig.d_theta_sptr_unset_processor_affinity(self)

    def processor_affinity(self):
        """processor_affinity(self) -> gr_vector_uint"""
        return _eecs_swig.d_theta_sptr_processor_affinity(self)

    def detail(self):
        """detail(self) -> gr_block_detail_sptr"""
        return _eecs_swig.d_theta_sptr_detail(self)

    def set_detail(self, *args, **kwargs):
        """set_detail(self, gr_block_detail_sptr detail)"""
        return _eecs_swig.d_theta_sptr_set_detail(self, *args, **kwargs)

    def name(self):
        """name(self) -> string"""
        return _eecs_swig.d_theta_sptr_name(self)

    def symbol_name(self):
        """symbol_name(self) -> string"""
        return _eecs_swig.d_theta_sptr_symbol_name(self)

    def input_signature(self):
        """input_signature(self) -> gr_io_signature_sptr"""
        return _eecs_swig.d_theta_sptr_input_signature(self)

    def output_signature(self):
        """output_signature(self) -> gr_io_signature_sptr"""
        return _eecs_swig.d_theta_sptr_output_signature(self)

    def unique_id(self):
        """unique_id(self) -> long"""
        return _eecs_swig.d_theta_sptr_unique_id(self)

    def to_basic_block(self):
        """to_basic_block(self) -> gr_basic_block_sptr"""
        return _eecs_swig.d_theta_sptr_to_basic_block(self)

    def check_topology(self, *args, **kwargs):
        """check_topology(self, int ninputs, int noutputs) -> bool"""
        return _eecs_swig.d_theta_sptr_check_topology(self, *args, **kwargs)

    def alias(self):
        """alias(self) -> string"""
        return _eecs_swig.d_theta_sptr_alias(self)

    def set_block_alias(self, *args, **kwargs):
        """set_block_alias(self, string name)"""
        return _eecs_swig.d_theta_sptr_set_block_alias(self, *args, **kwargs)

    def _post(self, *args, **kwargs):
        """_post(self, pmt_t which_port, pmt_t msg)"""
        return _eecs_swig.d_theta_sptr__post(self, *args, **kwargs)

    def message_ports_in(self):
        """message_ports_in(self) -> pmt_t"""
        return _eecs_swig.d_theta_sptr_message_ports_in(self)

    def message_ports_out(self):
        """message_ports_out(self) -> pmt_t"""
        return _eecs_swig.d_theta_sptr_message_ports_out(self)

d_theta_sptr_swigregister = _eecs_swig.d_theta_sptr_swigregister
d_theta_sptr_swigregister(d_theta_sptr)

d_theta_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
d_theta = d_theta.make;



