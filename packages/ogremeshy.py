#!/usr/bin/env python

import package_helpers

class PackageDetails( package_helpers.PackageTemplate ):
    name = 'Ogre Meshy'
    dirname = 'ogremeshy'

    def source( self, source_dir ):
        package_helpers.mercurial_clone( source_dir, self.dirname, [ 'https://bitbucket.org/dark_sylinc/ogremeshy/' ] )

