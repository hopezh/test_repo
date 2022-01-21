import torch

x = torch.rand( 5 , 8 )
print(x, '\n')

y = torch.ones(2, 3)
print(y, '\n')

print('cuda available: ', torch.cuda.is_available(), '\n')
