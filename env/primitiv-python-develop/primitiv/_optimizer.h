/* Generated by Cython 0.29.1 */

#ifndef __PYX_HAVE__primitiv___optimizer
#define __PYX_HAVE__primitiv___optimizer


#ifndef __PYX_HAVE_API__primitiv___optimizer

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#ifndef DL_IMPORT
  #define DL_IMPORT(_T) _T
#endif

__PYX_EXTERN_C int primitiv_python_optimizer_configure_parameter(PyObject *, primitiv::Parameter &);
__PYX_EXTERN_C int primitiv_python_optimizer_update_parameter(PyObject *, float, primitiv::Parameter &);
__PYX_EXTERN_C int primitiv_python_optimizer_get_configs(PyObject *, std::unordered_map<std::string,unsigned int>  &, std::unordered_map<std::string,float>  &);
__PYX_EXTERN_C int primitiv_python_optimizer_set_configs(PyObject *, std::unordered_map<std::string,unsigned int>  const &, std::unordered_map<std::string,float>  const &);

#endif /* !__PYX_HAVE_API__primitiv___optimizer */

/* WARNING: the interface of the module init function changed in CPython 3.5. */
/* It now returns a PyModuleDef instance instead of a PyModule instance. */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC init_optimizer(void);
#else
PyMODINIT_FUNC PyInit__optimizer(void);
#endif

#endif /* !__PYX_HAVE__primitiv___optimizer */