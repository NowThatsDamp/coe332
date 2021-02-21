# Homework 2
  This folder contains the updated read_animals script. The new functionality includes 2 new flags:
- The -H flag allows you to choose the head shape of the pulled animal.
- The -i flag allows you to cose the index of the pulled animal, i.e the first animal on the list, or the second, ect. When combined with the -H flag, the -i flag chooses which animal to pull relative to that head, i.e the first animal with a snake head, or the second animal with a snake head, ect.
- Using the -H flag without the -i flag will return the first animal on the list with that head
- Using no flags will return a random animal
  Note that the test script only works with the provided animals.json file. Generating a new one will cause the test script to throw failures. That is why the generation script is not included in this portion of the repo.
  
  All of the necessary files to build the Dockerfile for these scripts, including the generate_animals script, is in the "Dockerfiles" folder. Note that the generate_animals and the read_animals scripts in the Dockerfile section are slightly modified from the ones in the main directory, and are not interchangeable. The generate and read animals scripts in the dockerile section both have a required positional argument which is the name of the animal list json file, as described in the class 'read the docs' docerfile lesson.
