#include <stdio.h>

#define MAXBUFFER 20

int main(){
  FILE * inputFile = fopen("./input.txt", "r");
  if(inputFile == NULL){
    printf("File not found");
    return 0;
  }
  char line[MAXBUFFER];
  char direction[MAXBUFFER];
  int value = 0, posx = 0, depth = 0, depth2 = 0, aim = 0;
  while(fgets(line, MAXBUFFER, inputFile) != NULL){
    sscanf(line, "%s %d\n", direction, &value);
    switch(direction[0]){
      case 'f':
          posx += value;
          depth2 += aim*value;
          break;
      case 'u':
          depth -= value;
          aim -= value;
          break;
      case 'd':
          depth += value;
          aim += value;
            break;
    }
  }
  fclose(inputFile);
  printf("%d\n", posx*depth);
  printf("%d\n", posx*depth2);
}
