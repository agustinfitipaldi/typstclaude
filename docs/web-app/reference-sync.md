# Reference Sync

Source: https://typst.app/docs/web-app/reference-sync/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Web App](/docs/web-app/)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference Sync](/docs/web-app/reference-sync/)

# Reference Sync

Managing [bibliographies](/docs/reference/model/bibliography/) by hand can be arduous. Fortunately,
great tools like Zotero and Mendeley have been developed specifically to help in
this process. With Typst Pro, you can link your Typst account to one of these
two services and take advantage of automatic synchronization between your
bibliography and a `.bib` file in your project.

## Linking your accounts

First, connect your Typst account with your Zotero or Mendeley account. To do
so, navigate from the dashboard to your account settings, by clicking on the
![Cogwheel](/assets/icons/16-settings.svg)
Cogwheel button in the sidebar or selecting "Typst > Account settings"
from the menubar.

Once you are there, scroll to the section "Connections to other services". Click
"Connect with Zotero" or "Connect with Mendeley" depending on which service you
want to use. Then, let Typst guide you through the process, until you reach the
"Connection complete" page. You can then close this tab to go back to your
settings, where it should now be indicated that your external account is
connected.

You can use this same settings page to disconnect your account at any time by
clicking the corresponding button. Note that when disconnecting your account,
the bibliography files in your Typst projects will no longer be synchronized
automatically and will become regular text files.

## Create a synchronized bibliography

Go back to your dashboard, and open a project. Unless it is already visible,
open the file browser by clicking the ![Explore files](/assets/icons/16-archive.svg) icon in the sidebar.

Next to the title of the file browser, there are a few buttons to create new
files and folders. Click the ![arrow down](/assets/icons/16-arrow-down.svg) Arrow to display advanced options.
In this menu, select "Sync from Zotero" or "Sync from Mendeley".

![The advanced option menu, including the two options to synchronize bibliographies](/assets/images/new-magic-file.png)

Select either of these, depending on the service you want to use. A window
opens, asking you for the name of the auto-synced file (you can of course rename
it or move it to another folder later). It also asks which part of your Zotero
or Mendeley collection to sync. Once you configured everything as you wished,
click "Create & sync".

## Disconnect and Force sync

The new file is now available, containing your bibliography in BibLaTeX format.
If you open it, you will notice that you cannot edit it, but that two extra
options are available in the toolbar: ![Disconnect](/assets/icons/16-unlink.svg)
Disconnecting the file or ![Force sync](/assets/icons/16-progress.svg) forcing synchronization. The former
will turn the file into a regular text file that you can edit, but which won't
be automatically synchronized anymore. The latter can be used to manually resync
the file when the automatic synchronization has not yet kicked in.

![The aforementioned
buttons, the first with a broken chain icon, the second with circling arrows,
and a bit of text saying "Last synced with Zotero 4 minutes ago"](/assets/images/reference-sync-toolbar.png)

Next to these two buttons, a timer indicates the last time the file was
synchronized. When your project is open, the file is automatically refreshed
every five minutes.

The synchronized bibliography file can be used like any other BibLaTeX file in
your project: Call the [`bibliography`](/docs/reference/model/bibliography/) function and start
[referencing](/docs/reference/model/ref/) your sources.

## Who can sync?

Note that Typst Pro is only necessary to create a synchronized bibliography.
Once the file exists, and as long as the person who created it has access to the
project, it will be synchronized automatically and can be read and
force-synchronized by any person with write access, regardless of whether they
have a Typst Pro subscription or not. If the person who created the file leaves
the project, your bibliography will be turned into a regular text file.

[![←](/assets/icons/16-chevron-right.svg)

Private PackagesPrevious page](/docs/web-app/private-packages/) [![→](/assets/icons/16-chevron-right.svg)

Git SyncNext page](/docs/web-app/git-sync/)