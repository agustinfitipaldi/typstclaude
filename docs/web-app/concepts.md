# Concepts

Source: https://typst.app/docs/web-app/concepts/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Web App](/docs/web-app/)
- ![](/assets/icons/16-chevron-right.svg)
- [Concepts](/docs/web-app/concepts/)

# Concepts

The Typst web application is organized into three main concepts: Projects,
users, and teams. This documentation page explains each of these concepts and
explains where you can find more information on each.

## Projects

Projects are where you work on your documents, write Typst markup, and download
PDFs. When clicking on a project in your Dashboard, the project opens in the
editor view. There are various ways of [starting a new project](/docs/web-app/creating-a-project).

Projects consist of one or multiple files. You can click the Box icon in the
sidebar of the editor view to list the files in the project in the file panel.
We differentiate between three file types:

- **Typst files:** These files end in `.typ` and contain Typst markup. You can
  edit them with your team in the editor view by clicking on them. You can also
  choose any Typst file as the previewed file. The Typst file chosen as the
  previewed file will also be used to export the project when you download the
  PDF.
- **Text files:** These are files with endings like `.csv`, `.svg`, `.json`, or
  `.bib`. Like Typst files, you can edit them live in the editor view.
- **Other files:** These are files like images (`.jpg`, `.png`, `.gif`, `.svg`)
  or fonts (`.ttf`, `.ttc`, `.otf`). For some formats, we give an overview of
  the contents of the file if click on them. You cannot edit files like this
  directly in the Typst web application. Instead, you can upload replacements to
  make changes. There is an exception for SVG files, that can be converted to
  editable text files (but converting back to a non-editable image is not
  possible).

You can share a project with other users through the "Share" modal, accessible
from the toolbar. When sharing a project, we create a link that allows anyone
who visits it to view and optionally edit the project. If the user of the link
was signed in, they will be added to the *project members.* Project members
retain access to a project even if the share link they originally used is
deleted. You can view and remove project members in the "Share" modal. If you
have a Typst Pro subscription, this modal also offers options to [invite by
email](/docs/web-app/invite-by-email) or to [share private packages](/docs/web-app/private-packages#private-packages-and-external-collaborators).

## Users

Everyone with a Typst account is a user. User can own projects and be members of
teams. When opening Typst, you can view the projects you own. The sidebar will
contain a list of the teams you are a member of.

Most settings, like whether spellcheck is enabled, and the text size and font in
the editor, are specific to your user account. Other settings, like the chosen
theme, are per-device. You can find the various settings associated with your
account by clicking the cogwheel in the sidebar to go to your Account Settings,
and by clicking the same icon in the editor view sidebar to adjust
editing-related settings.

Users can enroll in Typst Pro to add additional features to their account and
receive more storage. Some features of their subscription carry over to the
people with whom they have shared projects, take a closer look at each of the
feature documentation pages for more details.

## Teams

Users in Typst can create and join teams to work jointly on a set of projects.
Just like a user, a team can own projects. You can switch to view the projects
one of your team owns by clicking its icon in the dashboard's sidebar. Each
member of the team will be able to create, edit, delete, and share projects as
if they were its owner.

You can add more users to a team by email address. When you invite a user on the
team settings page, they are sent an email to the address you entered. When they
sign into a Typst account with a matching email address, they see your invite
and can accept or decline it.

Each member of the team can optionally be an administrator. Only administrators
can invite and remove team members and promote them to administrators or demote
them to members.

Teams will receive access to editing-bound Typst Pro features like comments if
at least one of its administrators is subscribed to Typst Pro.

[![←](/assets/icons/16-chevron-right.svg)

Web AppPrevious page](/docs/web-app/) [![→](/assets/icons/16-chevron-right.svg)

Creating a ProjectNext page](/docs/web-app/creating-a-project/)