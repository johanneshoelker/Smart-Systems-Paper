cd Workspace
while find . -name '*.tex' | xargs inotifywait -qqre modify .; do \
  ./latex_build.sh; \
done
