FROM gitpod/workspace-full

# Install LaTeX
RUN sudo apt-get -q update && \
    sudo apt-get install -yq texlive-full inotify-tools pandoc && \
    sudo rm -rf /var/lib/apt/lists/*