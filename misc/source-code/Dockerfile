FROM ubuntu:latest

# Install OpenSSH server
RUN apt-get update && apt-get install openssh-server gcc -y

# Create a new user to connect to SSH with and set the password
RUN useradd -ms /bin/bash ctfsolver
RUN echo "ctfsolver:beginner101" | chpasswd

# Create a new user to be the owner of flag.c and set an unguessable password
RUN useradd -ms /bin/bash flagholder 
RUN echo "flagholder:ELBf3HK4qi7LrIc2HuBXPaDby7rkZCeq4xZq4q8vtWyKuzrVWD" | chpasswd

# Create the SSH user's directories
RUN mkdir -p /home/ctfsolver/.ssh/

# Create and set /challenge as working directory
WORKDIR /home/ctfsolver/challenge/

# Copy the challenge files across
COPY ./src/flag.c ./src/source_code.c ./

# Compile source_code
RUN gcc -o ./source_code ./source_code.c

# Set owner of files to be flagholder
RUN chown flagholder ./source_code ./source_code.c ./flag.c

# Make source_code world execute only + SUID
RUN chmod 4711 ./source_code

# Make source_code.c world read only
RUN chmod 744 ./source_code.c

# Make flag.c unreadable
RUN chmod 700 ./flag.c

# Disable default MOTD
RUN touch /home/ctfsolver/.hushlogin

# Make SSH user default to challenge directory
RUN echo "cd /home/ctfsolver/challenge/" >> /home/ctfsolver/.bashrc

# Start SSH service
RUN service ssh start

# Expose docker port 22
EXPOSE 22

# Start the SSH service
CMD ["/usr/sbin/sshd", "-D"]