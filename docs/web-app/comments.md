# Comments

Source: https://typst.app/docs/web-app/comments/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Web App](/docs/web-app/)
- ![](/assets/icons/16-chevron-right.svg)
- [Comments](/docs/web-app/comments/)

# Comments

Document creation is a collaborative process. Documents are often written by
teams, but even if you're working by yourself, you might want someone else to
proofread what you've written.

Typst Pro's comments are a great way for other people to give feedback on your
document. They can be attached to a range of text and stick to it as you're
collaboratively editing the document. Comments will be highlighted in the editor
with a yellow background and a little comment icon in the gutter (where the line
numbers are located).

If the Improve panel is open, clicking on commented text in the editor will
reveal and highlight it. If the Improve panel is closed, a hovering comment box
will instead appear over the editor. You can interact with it to edit, resolve,
delete, or reply to the comment.

![A Typst editor with part of an equation highlighted. Attached to the highlight, a hovering box with a comment thread. The first message says 'This doesn't look quite right. 🤔' and the reply is 'Hmm, maybe you're right.'](/assets/images/comment-box.png)

## Creating a comment

To create a new comment, select a range of text and click on the ![Add comment](/assets/icons/16-add-comment.svg) "Add
comment" button in the toolbar above the text editor. A hovering text box
will appear. After you've entered your thoughts, you can confirm the comment by
clicking the ![Checkmark](/assets/icons/16-check.svg)
Checkmark button or pressing Enter. To abort the edit, click the ![Cancel](/assets/icons/16-close.svg) Cancel button or
press Escape.

## Who can comment?

Whether comments are enabled for a project is decided by the subscription level
of the project owner. As long as the project owner (or in the case of a team an
administrator) has Typst Pro, collaborators can leave comments even if they
don't have Typst Pro.

Still, to leave comments, collaborators need a Typst account and review
permissions to the project. This includes people who have a "Review" access, but
also those with "Write" rights. You can grant review-only access with a
review-only share link, or by selecting "Review" when inviting someone by
e-mail. Note that leaving comments through an anonymous share link is not
possible.

## Replying to a comment

Sometimes, a bit of discussion is needed to figure out the best edit to your
document. When there's a little more to say, just click into the "Reply…" box
and start typing. To send your reply, click on the ![Reply](/assets/icons/16-reply.svg) Reply button or
press Enter.

## Resolving a comment

Once you've addressed a comment, you can click on the ![Create comment](/assets/icons/16-check.svg) Checkmark
button in the bottom right of the comment box. This *resolves* the comment,
hiding it from the comment list, while keeping it archived for future reference.

If a file contains at least one resolved comment, a new "Show resolved" checkbox
will appear next to its file name in the Improve panel. You can use this
checkbox to browse through already resolved comments. If you decide that a
comment isn't quite addressed yet after all, click the ![Unresolve comment](/assets/icons/16-regex.svg) Star
button in the bottom right corner of the comment box to unresolve the comment.

Any collaborator with write permission can resolve comments.

## Editing a comment or reply

If you notice a small mistake or have another thought after creating a comment
or reply, you can edit it. To do so, hover over the comment or reply and then
click on the ![Edit](/assets/icons/16-pencil.svg)
Pencil button that appears. Alternatively, perform a right-click and
select "Edit".

Then, tweak the text that appears in the text box at the bottom and click ![Apply edit](/assets/icons/16-reply.svg) "Apply edit"
or press Enter. To abort your edit, you can use the Escape key.

Only the creator of a comment can edit it. The project owner (in case it is
someone else) or unrelated collaborators cannot.

## Deleting a comment or reply

To delete a comment, click the ![Delete comment](/assets/icons/16-trash.svg) Trash button in the bottom right of
the comment box twice or right-click the comment and select "Delete". To delete
a comment reply, right-click it and select "Delete".

Deleting a comment is permanent and cannot be undone. If you've addressed a
comment but would like to keep it for future reference, you can resolve it
instead of deleting it. See ["Resolving a comment"](#resolving-a-comment) for
more details.

A comment can only be deleted by the person that created the comment or by the
project owner. It cannot be deleted by unrelated collaborators.

## Jumping to a comment

You can jump to the source location of a comment by clicking on the "Line …"
text in the top right of the comment box.

![A comment box with the mouse cursor hovering over the text 'Line 3', ready to click](/assets/images/comment-jump.png)

## Further Notes

- There is a limit of 1,000 comments and replies per project. Both unresolved
  and resolved comments count towards this limit, so you can regain space by
  deleting resolved comments.
- Comments will not be included in the PDF output.

[![←](/assets/icons/16-chevron-right.svg)

FoldersPrevious page](/docs/web-app/folders/) [![→](/assets/icons/16-chevron-right.svg)

Private PackagesNext page](/docs/web-app/private-packages/)