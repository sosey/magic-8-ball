# These are git alias which others have found useful

### Create a color coded, summary,  log listing for a repository, including branch graphs:
alias gitlog="git log --graph --oneline --decorate --pretty=format:'%C(green)%h %C(red)%ar %C(blue)%an %C(black)%s'"

### show the tracking branch for each local branch
alias gittrack="git for-each-ref --format='%(refname:short) <- %(upstream:short)' refs/heads"


