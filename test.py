import torch

x = torch.rand( 5 , 8 )

print(x)

print('cuda available: ' , torch.cuda.is_available() )
