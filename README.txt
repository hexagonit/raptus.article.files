Introduction
============

Provides support for adding attachments to articles.

The following features for raptus.article are provided by this package:

Content
-------
    * File - add files in an article.

Components
----------
    * Attachments (List of files contained in the article)
    
Dependencies
------------
    * raptus.article.core

Installation
============

Note if you install raptus.article.default you can skip this installation steps.

To install raptus.article.files into your Plone instance, locate the file
buildout.cfg in the root of your Plone instance directory on the file system,
and open it in a text editor.

Add the actual raptus.article.files add-on to the "eggs" section of
buildout.cfg. Look for the section that looks like this::

    eggs =
        Plone

This section might have additional lines if you have other add-ons already
installed. Just add the raptus.article.files on a separate line, like this::

    eggs =
        Plone
        raptus.article.files

Note that you have to run buildout like this::

    $ bin/buildout

Then go to the "Add-ons" control panel in Plone as an administrator, and
install or reinstall the "raptus.article.default" product.

Note that if you do not use the raptus.article.default package you have to
include the zcml of raptus.article.files either by adding it
to the zcml list in your buildout or by including it in another package's
configure.zcml.

Usage
=====

Add file
--------
You may now add files in your article. Click the "Add new" menu and select "File" in the pull down menu.
You get the standard plone form to add your file. 

Components
----------
Navigate to the "Components" tab of your article, select the attachments component
and press "save and view". Note that at least one file has to be contained
in the article in which this component is active.

Copyright and credits
=====================

raptus.article is copyrighted by `Raptus AG <http://raptus.com>`_ and licensed under the GPL. 
See LICENSE.txt for details.
