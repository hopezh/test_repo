import torch

x = torch.rand( 5 , 8 )
print(x)

y = torch.ones(2, 3)
print(y)

print('cuda available: ', torch.cuda.is_available())
