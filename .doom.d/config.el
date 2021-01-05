;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

(setq user-full-name "Nikola Drakulic"
      user-mail-address "ninadrakulic04@gmail.com")




(setq doom-font (font-spec :family "monospace" :size 14))


(setq doom-theme 'doom-vibrant)


(load-file "~/.doom.d/discord-emacs.el/discord-emacs.el")
(discord-emacs-run "384815451978334208")


(setq display-line-numbers-type t)

;; ORG mod

(setq org-directory "~/home/Dropbox/org"
      org-image-actual-width nil
      +org-export-directory "~/home/Dropbox/org/export"
      org-default-notes-file "~/home/Dropbox/org/personal/inbox.org"
      org-id-locations-file "~/home/Dropbox/org/.orgids"
      org-agenda-files (directory-files-recursively "~/home/Dropbox/org/" "\\.org$")
      ;; org-export-in-background t
      org-catch-invisible-edits 'smart)

;; Bookmark funcions add and list bookmakrs
(map! :leader
      :desc "List bookmarks"
      "b L" #'list-bookmarks
      :leader
      :desc "Save current bookmarks to bookmark file"
      "b w" #'bookmark-save)

;; Dired functions
(map! :leader
      :desc "Dired"
      "d d" #'dired
      :leader
      :desc "Dired jump to current"
      "d j" #'dired-jump
      (:after dired
        (:map dired-mode-map
         :leader
         :desc "Peep-dired image previews"
         "D p" #'peep-dired
         :leader
         :desc "Dired view file"
         "d v" #'dired-view-file)))
;; Make 'h' and 'l' go back and forward in dired. Much faster to navigate the directory structure!
(evil-define-key 'normal dired-mode-map
  (kbd "h") 'dired-up-directory
  (kbd "l") 'dired-open-file) ; use dired-find-file instead if not using dired-open package
;; If peep-dired is enabled, you will get image previews as you go up/down with 'j' and 'k'
(evil-define-key 'normal peep-dired-mode-map
  (kbd "j") 'peep-dired-next-file
  (kbd "k") 'peep-dired-prev-file)
(add-hook 'peep-dired-hook 'evil-normalize-keymaps)
;; Get file icons in dired
(add-hook 'dired-mode-hook 'all-the-icons-dired-mode)
;; With dired-open plugin, you can launch external programs for certain extensions
;; For example, I set all .png files to open in 'sxiv' and all .mp4 files to open in 'mpv'
(setq dired-open-extensions '(("gif" . "sxiv")
                              ("jpg" . "sxiv")
                              ("png" . "sxiv")
                              ("mkv" . "mpv")
                              ("mp4" . "mpv")))
(after! latex
  (defun azy2/compile-pdf ()
    (setq-local compilation-scroll-output t)
    (compile (concat "pdflatex " (file-name-nondirectory buffer-file-name))))
  (add-hook 'LaTeX-mode-hook
    '(lambda () (add-hook 'after-save-hook 'azy2/compile-pdf nil 'local))))
 (add-hook 'doc-view-mode-hook #'auto-revert-mode)

;; (def-package! org-ref
;;     :after org
;;     ; code to run before loading org-ref
;;     :config
;;         (setq reftex-default-bibliography '("~/Dropbox/bibliography/references.bib"))
;;     ; code to run after loading org-ref
;;     )
