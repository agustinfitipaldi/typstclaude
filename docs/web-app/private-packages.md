# Private Packages

Source: https://typst.app/docs/web-app/private-packages/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Web App](/docs/web-app/)
- ![](/assets/icons/16-chevron-right.svg)
- [Private Packages](/docs/web-app/private-packages/)

# Private Packages

Packages from [Typst Universe](https://typst.app/universe) bring rich automations to your
documents. With Typst Pro's private packages, we bring the same power to your
personal and team workspaces.

Private packages let you share and reuse code and assets across all of your
projects. Meanwhile, with private templates, you can build your own collection
of document types and reuse them across your projects.

Private packages and templates are easy to publish and manage, directly from the
editor. They are only accessible to yourself, or in case of a private package
owned by a team, by other members of your team.

This documentation focuses on private packages in the web application. For more
information about package authoring we recommend reading our [general packaging
documentation](https://github.com/typst/packages/blob/main/README.md).

## Creating a private package

The first step in creating a private package is to start a new project that will
contain your package files. If you have an existing project that you want to
turn into a package, that is also possible.

In the project, select "File > Package project" from the menu bar or "Create
package manifest" from the dropdown menu next to the file and folder creation
buttons. This creates a new file called `typst.toml` in the root folder of your
project. This file is your package manifest and contains the package's metadata.
For more details about specific fields, please refer [to our packaging
documentation](https://github.com/typst/packages/blob/main/README.md).

Open the manifest. You should be presented with the following form.

![A two column interface. On the left a form to edit package metadata, on the right a list of published package version, currently empty.](/assets/images/private-package-manifest.png)

Using this interface, you can configure your package metadata before
publication. If you prefer to write [TOML](https://toml.io/) directly, you can switch to a
code editor using the dedicated button in the top left corner of the form.

Once you are ready to publish a first version, click the "Publish" button in the
top right. To publish new versions, once you made changes to the contents of
your package, change the version number in the manifest, and click "Publish"
again.

You can delete a published version of a package, but note that if another
project depends on it, it will no longer be able to import it and will thus
break.

## Importing and using a package

Once you have published a private package, you can import it in other projects.
Open a Typst file in another project, and add an import for
`"@local/{package-name}:{version}"`. Just like public packages, you can choose
what to import and under which name.

```typst
// Import the whole package ...
#import "@local/package-demo:0.1.0"
#package-demo.a-function()

// ... or only specific items.
#import "@local/package-demo:0.1.0": a-function
#a-function()
```

## Private templates

A private package can also expose a template. For that, check the "This package
is a template" box in the manifest form (or add a `template` section to the
TOML file).

![The bottom section of the manifest form, dedicated to configuring the template](/assets/images/private-package-template.png)

If you don't yet have a sub-directory to store your template files, you will
have to create one. This sub-directory will be copied as-is to projects created
from the template. In particular, this means that you should take care of using
package-style imports in the template and not relative ones: The files outside
of the template sub-directory will not be copied into other projects and
referencing them using their paths will not work. To make this more convenient,
the web app compiler is configured to support package-style imports for the
current version of the package you are working on, even if it is not yet
released.

Once published, your private template will be available to create new projects,
either from the "Start from template" button at the top of the project list on
the dashboard, or below on the same page, using the dedicated button on the
corresponding package card.

## Private packages and external collaborators

Generally, private packages are only available to yourself or other members of
your team (in case the package is owned by a team). However, Typst also allows
sharing a project with external collaborators. When sharing a project, read-only
access to packages that are currently used in the project will be automatically
granted.

You can choose to give access to more packages, or to restrict access to some
packages that you consider too confidential to share with external
collaborators. In the latter situation, this will probably mean that the
document will not compile for these persons, so they will neither have access to
real-time previews nor to auto-completion features.

To choose which packages to share or not, open the "Share" modal, using the
dedicated button in the top right corner. You can then click on a specific
package to share or unshare it. You can also use the "all", "none" and "recently
used packages" shortcuts at the bottom of the list to quickly select the
corresponding packages.

![The section of the "Share" modal dedicated to sharing package, showing a list of two packages, one that is shared and the other not.](/assets/images/private-package-share.png)

The version indicated in the list is the latest version of the package and is
only displayed for informational purposes. When sharing a package, all versions
will be available to your collaborators.

Note that these settings are on a per-project basis, and that only read access
to private packages is granted to external project members.

[![←](/assets/icons/16-chevron-right.svg)

CommentsPrevious page](/docs/web-app/comments/) [![→](/assets/icons/16-chevron-right.svg)

Reference SyncNext page](/docs/web-app/reference-sync/)