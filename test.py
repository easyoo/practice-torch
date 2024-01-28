import torch

# construct a tensor with data or shape
a = torch.tensor([1, 2, 3],dtype=float, device='cuda' if torch.cuda.is_available() else 'cpu', requires_grad=True)
b = torch.zeros(1,2,3)
c = torch.zeros([1,2,3])
d = torch.eye(4)    # 对角矩阵
e = torch.empty(2,3)
f = torch.rand(3,4)
g = torch.randn(2,3)
h = torch.arange(20)
h1 = h[:5]
print(h,h1)

# other Ops
x = torch.randn(2,3)
a1 = torch.cat((x,x),1)
a2 = torch.reshape(x,(3,-1))


