while find . -name '*.tex' | xargs inotifywait -qqre modify .; do \
  cd Workspace
  ./latex_build.sh; \
done
