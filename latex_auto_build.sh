cd Workspace

while find . -name '*.tex' | xargs inotifywait -qqre modify .; do \
  clear
  echo "A Latex file was saved and the building process is started..."
  ./latex_build.sh
  clear
  echo "Build process finished successfully."
  echo "Waiting for new changes...."; \
done
