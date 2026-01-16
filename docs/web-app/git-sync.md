# Git Sync

Source: https://typst.app/docs/web-app/git-sync/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Web App](/docs/web-app/)
- ![](/assets/icons/16-chevron-right.svg)
- [Git Sync](/docs/web-app/git-sync/)

# Git Sync

A Typst project can be linked to a [Git](https://git-scm.com/) repository hosted on GitHub or
GitLab. This allows you to pull and push changes between the Typst web app and
the remote repository. Using the Git integration, you can keep track of your
project's history if you also use Typst outside of the web application and
collaborate with people who are using Typst locally.

From the Typst web app, you can connect your github.com or gitlab.com account.
Other forges are not currently supported. If you host Typst on-premises, your
administrator can configure different URLs for these two services,
enabling connections to a GitHub Enterprise instance or a self-hosted GitLab.

Typst Pro is necessary only to link a project to a repository, pushing and
pulling changes can be done by any person with write access to the project.

Note that the Git integration is still experimental and that we are continually
improving it. It is possible that you encounter bugs. That said, we will never
force push and overwrite your Git history.

## Connect your accounts

The first step to use Git synchronization is to connect your GitHub or GitLab
account (or both). To do so, navigate from the dashboard to your account
settings, by clicking on the ![Cogwheel](/assets/icons/16-settings.svg) Cogwheel
button in the sidebar or selecting "Typst > Account settings" from the menubar.

On the settings page, scroll to the "Connections to other services" section.
Here, click on "Connect with GitHub" or "Connect with GitLab". Then, follow the
process until you arrive on the "Connection complete" page. Once you are there,
you can close this tab to get back to the settings page. Your accounts are now
linked!

You can disconnect your account at any time from this same settings page. When
doing so, projects that you linked to a remote repository using your account
will not be able to synchronize anymore. However, it will be possible to
[reconnect them with another account](#disconnecting-and-re-connecting-a-project), or your own account if you
decide to restablish the link between your Typst and GitHub/GitLab accounts.

## Connect a project with Git

Now that you have connected your GitHub or GitLab account, you can use it to
sync a project with a Git repository.

To clone a Git repository as **a new project**, you can use the [dedicated
option on the dashboard](/docs/web-app/creating-a-project#create-a-project-from-a-git-repository).

To connect **an existing project**, go to its settings, by clicking the ![Cogwheel](/assets/icons/16-settings.svg) Cogwheel
button in the bottom part of the sidebar. At the bottom of the settings side
panel, you will find a "Version control" section with a button to link your
project to a remote repository. Click it and fill the form.

It is not possible to create a repository from this dialog. You will have to
create it beforehand in GitHub or GitLab. Also note that it is not possible to
connect your project to a non-empty directory of your repository, as that could
result in conflicts. If you don't have an empty directory available, you can create
a new branch dedicated to your project, which won't share any history with other
parts of the repository, or create a new directory just for your Typst files.

Once ready, click on "Link". Your project is now connected, as shown in the
"Version control" section of the settings panel.

Notice the two buttons that appeared above the preview. The one on the left is
for pulling and will indicate how many commits were made on the remote
repository since the last pull (if any), the one on the right can be used to
push changes. It indicates the duration since the last push.

![A zoom on the top bar of the editor, focusing on the two aforementioned buttons. The one one the left has an arrow icon pointing down, and next to it a "1" in a blue circle. The other one has an arrow pointing up, and a gray badge reading "36m".](/assets/images/git-sync-buttons.png)

## Pulling changes

To fetch changes that were made to the remote Git repository and include them in
your Typst project, click the ![Arrow down](/assets/icons/16-downgrade.svg) Pull button. Typst will need a few
seconds to process the changes, but will eventually incorporate them.

### Conflicts

On the level of textual file contents, our Git synchronization process is
conflict-free. If you added a new paragraph at the end of your document, and
someone else did the same in the remote repository, both paragraphs will be
present after pulling changes. You may still need to review the merged document
to switch their order or replace them with a synthesis of the two, but your file
contents will never be in a "conflicted" state that prevents you from working.

That said, there are a few cases in which Typst will show you a modal while
processing remote changes, asking you how to handle conflicts for specific
files:

- **If a file was deleted in the repository but modified in Typst**: we don't
  want you to lose changes because of that, so we ask for a confirmation that
  the file should be deleted. In the opposite situation (a file is deleted in
  Typst but was modified on Git's side), we delete the file in the repository,
  but if this was a mistake, you can leverage the Git history to recover.
- **If a non-text file was updated on both sides**: Typst can't automatically
  merge two images or more generally binary files together, so it asks which
  version to keep. If you need a synthesis of the two files, choose either
  version, and then manually create and upload a new version that takes into
  account both changes.
- **If a file was created both in Typst and in Git**: because the files have no
  shared history, it doesn't make sense to merge them together.

### Forbidden files

Some files that are present in your Git repository may not be visible in Typst
even after pulling the latest changes. This is because Typst has some
restrictions on the formats of files you upload. Archive files (`.zip`, `.tar`,
etc.) and executables, for instance, are forbidden.

These files will be left as-is in the repository when pushing. They won't be
deleted even if they don't appear in Typst's copy of the project.

## Pushing changes

When you want to commit and push changes you made in the Typst editor to your
Git repository, click the ![Arrow up](/assets/icons/16-upgrade.svg) Push button. A modal opens, asking you
for a commit message and email address to use for the commit. Addresses that you
associated with your Typst account and your GitHub or GitLab account will be
available. To confirm, click "Push".

In case someone else pushed commits to the repository before you, you will be
asked to pull these changes first. Use the dedicated button for that (see
above). Then, push again.

## Disconnecting and reconnecting a project

If the person who connected a project to Git using their account leaves the
project or dissociates their Git and Typst accounts, it will no longer be
possible to push and pull changes.

In that case, another user with an associated Git account can go to the project
settings page, and click "Reconnect with my account". For that option to work
correctly, you must have the right to push to the Git repository.

If you want to entirely disconnect a project, you can use the "Disconnect from
GitHub" (or "Disconnect from GitLab") button, in the same section of the project
settings. Note that if you do that, you will of course no longer be able to
synchronize your project with the repository, but you will not be able to
reconnect it with the exact same settings later, unless you delete all the files
from the synced directory in the Git repository. This is for the same reason
that you cannot connect an existing project to a non-empty directory: It would
be impossible for Typst to tell which version of a file to keep in case of a
conflict, because the two versions of the project share no history.

[![←](/assets/icons/16-chevron-right.svg)

Reference SyncPrevious page](/docs/web-app/reference-sync/) [![→](/assets/icons/16-chevron-right.svg)

Presentation ModeNext page](/docs/web-app/presentation-mode/)