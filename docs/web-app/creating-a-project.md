# Creating a Project

Source: https://typst.app/docs/web-app/creating-a-project/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Web App](/docs/web-app/)
- ![](/assets/icons/16-chevron-right.svg)
- [Creating a Project](/docs/web-app/creating-a-project/)

# Creating a Project

Projects are where you write Typst and collaborate with your team. There are six
ways to start a project:

- Create an empty project
- Create a project from a template on [Typst Universe](https://typst.app/universe/)
- Create a project from one of [your private templates](/docs/web-app/private-packages#private-templates)
  (with Typst Pro)
- Create a project using a custom template with the template wizard
- Create a project by converting other files like LaTeX and Word to Typst
- Create a project by cloning a repository on GitHub or GitLab (with Typst Pro)

If you are just starting out with Typst, going with a template from Typst
Universe is a great choice!

No matter which method you choose, go to your [Typst
dashboard](https://typst.app/app) to get started. If you want to create the
project within a team, choose the right team from the sidebar first. If you want
to create a personal project, be sure that your workspace is selected in the
sidebar. It is the round icon at the top of the sidebar and selected by default.

Once you are in the right workspace, locate the two big buttons at the top of
your dashboard:

![Two large buttons, side by side. The first one says "Empty document", the second "Start from template"](/assets/images/dashboard-create-project.png)

The left button will always create a new empty project while the right button
shows the most recent method you used to create a pre-populated project. You can
click the dropdown arrow on the right to choose one of the other methods for
project creation. When clicking on any of the buttons, a dialog that will ask
you for the name of the project will open. Depending on which method you chose,
the dialogue may ask for additional configuration. The following sections
explain how to use these dialogs.

## Creating a project from a template

The Typst community has created some great templates that you can use to get
started quickly with a new project. Choose "Start from template" from the
dropdown menu of the project creation button on your dashboard. Next, Typst will
present you with a dialog containing all of the available templates. Click on a
template to select it and enter a project name in the bottom right text field,
then press the "Create" button to create your project.

There are a few features that help you to choose the right template. First, you
can hover any template thumbnail and click the magnification glass icon to
display a larger preview. You can also search templates for keywords or filter
them by category and academic discipline using the search bar and the two
dropdowns at the top of the dialog, respectively.

Some template names are marked up with an icon. Here's what these icons mean:

- ![Lock](/assets/icons/16-lock.svg)
  These templates are [private](/docs/web-app/private-packages#private-templates), only you can see them. If you
  are in a team, other members of the team can also see them.
- ![Star](/assets/icons/16-star.svg)
  These templates are featured by the Typst team because they are especially
  high-quality.
- ![Verified](/assets/icons/16-verified.svg)
  These templates have been endorsed by members of the organization that the
  template is for (e.g. the publisher for a paper template or a university for a
  thesis template).

You can also go to a template's page on Typst Universe and click the "Create
project in app" button in the sidebar to directly jump to this dialog with the
right template selected.

## Create a project with a custom template

You can use the template wizard to customize your project setup for prose-heavy
documents like reports, theses, books, and papers. This dialog allows you to
customize a template by selecting between a few options for appearance and
structure. Choose "Customize a template" from the dropdown menu of the project
creation button on your dashboard.

On the first page, you can choose the title of the project (which will also
become the project title), how it is displayed, and add details about you and
your co-authors. You can add and remove additional authors, but there must be at
least one. The preview on the left updates as you customize these settings.

Once you have provided a title, you can go to the next page by clicking "Next".
There, you can control the page, paragraph, and text setup. Try each of the
options to learn what impact it has on the preview. Once you are happy with the
result, press "Create".

## Create a project by converting other files

If you have a document in another format on your computer and you would like to
convert it to Typst, you can select the "Start from a file" option.

Choose a project name, and pick a file to convert. Markdown, LaTeX, Word, and
OpenDocument Text files are supported.

This feature is still experimental. For the time being, only one source file can
be uploaded. Also, note that images are not currently automatically extracted
from the original document. You will have to upload them manually once the
project is created.

## Create a project from a Git repository

If you have a Typst Pro subscription, and if you have [linked either your GitHub
or GitLab account](/docs/web-app/git-sync#connect-your-accounts) in your personal settings, you can use the "Start
from GitHub" or "Start from GitLab" buttons, respectively. If you don't have
Typst Pro or didn't yet connect your external accounts, you can still use these
options, they will guide you through the process of registering for Typst Pro
and linking your accounts.

Both modals offer the same options. You can choose a name for your project, and
choose which repository to clone, first by selecting its owner in the first
dropdown menu (either your personal account or one of the organizations you are
part of), and then by picking a specific repository using the second dropdown.
When using GitHub, it can happen that an organization or repository doesn't
appear in the list even when it should. Head to [this settings
page](https://github.com/settings/connections/applications/Ov23li52NESd9bjas5D5) to change that by granting access to the corresponding
organization.

Below, you can unfold the "Advanced options" section to choose which branch and
sub-directory to clone. You can also let Typst create a new branch that won't
have any shared history with the rest of the repository, or a new directory in
which your project will live. When cloning a sub-directory, no other file will
be accessible to Typst at all, so if you want to reference images or data files
that are stored in other parts of your repository, clone the whole repository
(or at least the smallest common ancestor). These settings cannot be changed
once the project is created.

Once you are ready, click "Create project". Cloning and importing the Git
repository can take a bit of time. More generally, please note that Git
synchronization is still considered experimental.

[![←](/assets/icons/16-chevron-right.svg)

ConceptsPrevious page](/docs/web-app/concepts/) [![→](/assets/icons/16-chevron-right.svg)

FoldersNext page](/docs/web-app/folders/)