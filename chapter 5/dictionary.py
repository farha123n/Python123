mydic={
      'fast':'a quick manner',
      "farhan":"a coder",
      'list':[1,3,6,4],
      'innerdic':{'farhan':'player'},

}
print(mydic['innerdic']['farhan'])
print(mydic.keys())# print the keys of the dictionary
print(mydic.values())# print the values of the dictionary
print(mydic.items())# print both the values and the keys of the dictionary
updatedic={
      'lovish':"friend",
}
mydic.update(updatedic) #add items of updatedic
print(mydic)
