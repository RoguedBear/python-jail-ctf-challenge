# \<figure out title later>
 
  ## How to use
  modify the ssh port if you wish in the docker-compose file
  1. deploy the container
  2. ssh into it using the user `user` and the password [hardcoded](https://github.com/RoguedBear/python-jail-ctf-challenge/blob/main/Dockerfile#L18)
    in the Dockerfile `password123` \
    example:
      ```
      $ ssh -p 5899 user@localhost
      ```
  3. $$$ hax $$$


  ## Config
  - to edit the welcome message shown on login (eg: to show instructions again) edit the `welcome_message.txt` file
  - edit the flag in `flag.txt`
