# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Flecsi(CMakePackage):
    '''FleCSI is a compile-time configurable framework designed to support
       multi-physics application development. As such, FleCSI attempts to
       provide a very general set of infrastructure design patterns that can
       be specialized and extended to suit the needs of a broad variety of
       solver and data requirements. Current support includes multi-dimensional
       mesh topology, mesh geometry, and mesh adjacency information,
       n-dimensional hashed-tree data structures, graph partitioning
       interfaces,and dependency closures.
    '''
    homepage = 'http://flecsi.lanl.gov/'
    git      = 'https://github.com/laristra/flecsi.git'

    version('develop', branch='feature/refactor', submodules=False, preferred=True)
    variant('backend', default='hpx', values=('serial', 'mpi', 'legion','hpx'),
            description='Backend to use for distributed memory')

    depends_on('cmake@3.1:',  type='build')
    depends_on('mpi', when='backend=hpx')
    depends_on('hpx@stable', when='backend=hpx')
    depends_on('metis@5.1.0:')
    depends_on('parmetis@4.0.3:')
    depends_on('caliper', when='+caliper')
    depends_on('graphviz', when='+graphviz')
    depends_on('python@3.0:', when='+tutorial')

    def cmake_args(self):
        options = ['-DCMAKE_BUILD_TYPE=debug']
        options.append('-DCINCH_SOURCE_DIR=' + self.spec['cinch'].prefix)

        if self.spec.variants['backend'].value == 'hpx':
            options.append('-DFLECSI_RUNTIME_MODEL=hpx')
            options.append('-DENABLE_MPI=ON')
            options.append('-DENABLE_OPENMP=ON')
            options.append('-DCXX_CONFORMANCE_STANDARD=c++17')
            options.append('-DFLECSI_RUNTIME_MODEL=hpx')
            options.append('-DENABLE_FLECSIT=OFF')
            options.append('-DENABLE_FLECSI_TUTORIAL=OFF')
            options.append('DENABLE_METIS=ON')
            options.append('DENABLE_PARMETIS=ON')
            options.append('DENABLE_COLORING=ON')
            options.append('DENABLE_UNIT_TESTS=ON')
            options.append('DENABLE_DEVEL_TARGETS=ON')
            options.append('DFLECSI_RUNTIME_MODEL=hpx')

        return options
