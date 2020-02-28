#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : semantic_version
Version  : 2.8.4
Release  : 32
URL      : https://files.pythonhosted.org/packages/67/24/7e8fcb6aa88bfc018f8e4c48c4dbc8e87d8c7b3c0d0d8b3b0c61a34d32c7/semantic_version-2.8.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/67/24/7e8fcb6aa88bfc018f8e4c48c4dbc8e87d8c7b3c0d0d8b3b0c61a34d32c7/semantic_version-2.8.4.tar.gz
Summary  : A library implementing the 'SemVer' scheme.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: semantic_version-license = %{version}-%{release}
Requires: semantic_version-python = %{version}-%{release}
Requires: semantic_version-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
python-semanticversion
======================

This small python library provides a few tools to handle `SemVer`_ in Python.
It follows strictly the 2.0.0 version of the SemVer scheme.

.. image:: https://secure.travis-ci.org/rbarrois/python-semanticversion.png?branch=master
    :target: http://travis-ci.org/rbarrois/python-semanticversion/

.. image:: https://img.shields.io/pypi/v/semantic_version.svg
    :target: https://python-semanticversion.readthedocs.io/en/latest/changelog.html
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/semantic_version.svg
    :target: https://pypi.python.org/pypi/semantic_version/
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/wheel/semantic_version.svg
    :target: https://pypi.python.org/pypi/semantic_version/
    :alt: Wheel status

.. image:: https://img.shields.io/pypi/l/semantic_version.svg
    :target: https://pypi.python.org/pypi/semantic_version/
    :alt: License

Links
-----

- Package on `PyPI`_: http://pypi.python.org/pypi/semantic_version/
- Doc on `ReadTheDocs <http://readthedocs.org/>`_: https://python-semanticversion.readthedocs.io/
- Source on `GitHub <http://github.com/>`_: http://github.com/rbarrois/python-semanticversion/
- Build on `Travis CI <http://travis-ci.org/>`_: http://travis-ci.org/rbarrois/python-semanticversion/
- Semantic Version specification: `SemVer`_


Getting started
===============

Install the package from `PyPI`_, using pip:

.. code-block:: sh

    pip install semantic_version

Or from GitHub:

.. code-block:: sh

    $ git clone git://github.com/rbarrois/python-semanticversion.git


Import it in your code:


.. code-block:: python

    import semantic_version



This module provides classes to handle semantic versions:

- ``Version`` represents a version number (``0.1.1-alpha+build.2012-05-15``)
- ``BaseSpec``-derived classes represent requirement specifications (``>=0.1.1,<0.3.0``):

  - ``SimpleSpec`` describes a natural description syntax
  - ``NpmSpec`` is used for NPM-style range descriptions.

Versions
--------

Defining a ``Version`` is quite simple:


.. code-block:: pycon

    >>> import semantic_version
    >>> v = semantic_version.Version('0.1.1')
    >>> v.major
    0
    >>> v.minor
    1
    >>> v.patch
    1
    >>> v.prerelease
    []
    >>> v.build
    []
    >>> list(v)
    [0, 1, 1, [], []]

If the provided version string is invalid, a ``ValueError`` will be raised:

.. code-block:: pycon

    >>> semantic_version.Version('0.1')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/Users/rbarrois/dev/semantic_version/src/semantic_version/base.py", line 64, in __init__
        major, minor, patch, prerelease, build = self.parse(version_string, partial)
      File "/Users/rbarrois/dev/semantic_version/src/semantic_version/base.py", line 86, in parse
        raise ValueError('Invalid version string: %r' % version_string)
    ValueError: Invalid version string: '0.1'


Obviously, ``Versions`` can be compared:


.. code-block:: pycon

    >>> semantic_version.Version('0.1.1') < semantic_version.Version('0.1.2')
    True
    >>> semantic_version.Version('0.1.1') > semantic_version.Version('0.1.1-alpha')
    True
    >>> semantic_version.Version('0.1.1') <= semantic_version.Version('0.1.1-alpha')
    False

You can also get a new version that represents a bump in one of the version levels:

.. code-block:: pycon

    >>> v = semantic_version.Version('0.1.1+build')
    >>> new_v = v.next_major()
    >>> str(new_v)
    '1.0.0'
    >>> v = semantic_version.Version('1.1.1+build')
    >>> new_v = v.next_minor()
    >>> str(new_v)
    '1.2.0'
    >>> v = semantic_version.Version('1.1.1+build')
    >>> new_v = v.next_patch()
    >>> str(new_v)
    '1.1.2'

It is also possible to check whether a given string is a proper semantic version string:


.. code-block:: pycon

    >>> semantic_version.validate('0.1.3')
    True
    >>> semantic_version.validate('0a2')
    False


Finally, one may create a ``Version`` with named components instead:

.. code-block:: pycon

    >>> semantic_version.Version(major=0, minor=1, patch=2)
    Version('0.1.2')

In that case, ``major``, ``minor`` and ``patch`` are mandatory, and must be integers.
``prerelease`` and ``patch``, if provided, must be tuples of strings:

.. code-block:: pycon

    >>> semantic_version.Version(major=0, minor=1, patch=2, prerelease=('alpha', '2'))
    Version('0.1.2-alpha.2')


Requirement specification
-------------------------

The ``SimpleSpec`` object describes a range of accepted versions:


.. code-block:: pycon

    >>> s = SimpleSpec('>=0.1.1')  # At least 0.1.1
    >>> s.match(Version('0.1.1'))
    True
    >>> s.match(Version('0.1.1-alpha1'))  # pre-release doesn't satisfy version spec
    False
    >>> s.match(Version('0.1.0'))
    False

Simpler test syntax is also available using the ``in`` keyword:

.. code-block:: pycon

    >>> s = SimpleSpec('==0.1.1')
    >>> Version('0.1.1-alpha1') in s
    True
    >>> Version('0.1.2') in s
    False


Combining specifications can be expressed as follows:

  .. code-block:: pycon

      >>> SimpleSpec('>=0.1.1,<0.3.0')


Using a specification
"""""""""""""""""""""

The ``SimpleSpec.filter`` method filters an iterable of ``Version``:

.. code-block:: pycon

    >>> s = SimpleSpec('>=0.1.0,<0.4.0')
    >>> versions = (Version('0.%d.0' % i) for i in range(6))
    >>> for v in s.filter(versions):
    ...     print v
    0.1.0
    0.2.0
    0.3.0

It is also possible to select the 'best' version from such iterables:


.. code-block:: pycon

    >>> s = SimpleSpec('>=0.1.0,<0.4.0')
    >>> versions = (Version('0.%d.0' % i) for i in range(6))
    >>> s.select(versions)
    Version('0.3.0')


Coercing an arbitrary version string
""""""""""""""""""""""""""""""""""""

Some user-supplied input might not match the semantic version scheme.
For such cases, the ``Version.coerce`` method will try to convert any
version-like string into a valid semver version:

.. code-block:: pycon

    >>> Version.coerce('0')
    Version('0.0.0')
    >>> Version.coerce('0.1.2.3.4')
    Version('0.1.2+3.4')
    >>> Version.coerce('0.1.2a3')
    Version('0.1.2-a3')


Including pre-release identifiers in specifications
"""""""""""""""""""""""""""""""""""""""""""""""""""

When testing a ``Version`` against a ``SimpleSpec``, comparisons are
adjusted for common user expectations; thus, a pre-release version (``1.0.0-alpha``)
will not satisfy the ``==1.0.0`` ``SimpleSpec``.

Pre-release identifiers will only be compared if included in the ``BaseSpec``
definition or (for the empty pre-release number) if a single dash is appended
(``1.0.0-``):


.. code-block:: pycon

    >>> Version('0.1.0-alpha') in SimpleSpec('<0.1.0')  # No pre-release identifier
    False
    >>> Version('0.1.0-alpha') in SimpleSpec('<0.1.0-')  # Include pre-release in checks
    True


Including build metadata in specifications
""""""""""""""""""""""""""""""""""""""""""

Build metadata has no ordering; thus, the only meaningful comparison including
build metadata is equality.


.. code-block:: pycon

    >>> Version('1.0.0+build2') in SimpleSpec('<=1.0.0')   # Build metadata ignored
    True
    >>> Version('1.0.0+build1') in SimpleSpec('==1.0.0+build2')  # Include build in checks
    False


NPM-based ranges
----------------

The ``NpmSpec`` class handles NPM-style ranges:

.. code-block:: pycon

    >>> Version('1.2.3') in NpmSpec('1.2.2 - 1.4')
    True
    >>> Version('1.2.3') in NpmSpec('<1.x || >=1.2.3')
    True

Refer to https://docs.npmjs.com/misc/semver.html for a detailed description of NPM
range syntax.


Using with Django
=================

The ``semantic_version.django_fields`` module provides django fields to
store ``Version`` or ``BaseSpec`` objects.

More documentation is available in the ``django`` section.


Contributing
============

In order to contribute to the source code:

- Open an issue on `GitHub`_: https://github.com/rbarrois/python-semanticversion/issues
- Fork the `repository <https://github.com/rbarrois/python-semanticversion>`_
  and submit a pull request on `GitHub`_
- Or send me a patch (mailto:raphael.barrois+semver@polytechnique.org)

When submitting patches or pull requests, you should respect the following rules:

- Coding conventions are based on ``8``
- The whole test suite must pass after adding the changes
- The test coverage for a new feature must be 100%
- New features and methods should be documented in the ``reference`` section
  and included in the ``changelog``
- Include your name in the ``contributors`` section

.. note:: All files should contain the following header::

          # -*- encoding: utf-8 -*-
          # Copyright (c) The python-semanticversion project


Contents
========

   :maxdepth: 2

   reference
   django
   changelog
   credits


.. _SemVer: http://semver.org/
.. _PyPI: http://pypi.python.org/

Indices and tables
==================

* ``genindex``
* ``modindex``
* ``search``

%package license
Summary: license components for the semantic_version package.
Group: Default

%description license
license components for the semantic_version package.


%package python
Summary: python components for the semantic_version package.
Group: Default
Requires: semantic_version-python3 = %{version}-%{release}

%description python
python components for the semantic_version package.


%package python3
Summary: python3 components for the semantic_version package.
Group: Default
Requires: python3-core
Provides: pypi(semantic-version)

%description python3
python3 components for the semantic_version package.


%prep
%setup -q -n semantic_version-2.8.4
cd %{_builddir}/semantic_version-2.8.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582923604
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/semantic_version
cp %{_builddir}/semantic_version-2.8.4/LICENSE %{buildroot}/usr/share/package-licenses/semantic_version/a70ef24806317169e4539b723cad891e08cf1783
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/semantic_version/a70ef24806317169e4539b723cad891e08cf1783

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
