from utils import *
from model import *
import os
import csv
import sys
import argparse
import yaml



def fingerprints(smiles):
    parser = argparse.ArgumentParser(description="Generate NNFP")
    parser.add_argument("input",type = str, help="Path to the input file.")
    parser.add_argument("output", type=str, help="Output path.")
    parser.add_argument("-s", "--smiles",default = "smiles", help="Name or number of column containing the SMILES string.")
    parser.add_argument("-m", "--model", default = "aux", choices=['aux', 'ae', 'base'],help="which model to use? ['aux', 'ae', 'base']")
    parser.add_argument("-n", "--no_header", default = "infer", action='store_const', const= None, help="Read in header")

    args = parser.parse_args()

    data = pd.DataFrame(smiles, columns=['smiles'])
    

    #convert colnumbers to int
    try:
        args.smiles=int(args.smiles)
    except:
        if (type(args.smiles) == str) & (args.no_header is None):
            print("\n ERROR: If you want to index the column containing the SMILES by name, then you need to keep the header! \n")
            exit()
        args.smiles  = np.where(data.columns== args.smiles)[0][0]



    model_paths = os.path.dirname(os.path.realpath(__file__))+"/../../../../checkpoints/data/trained_models/npl_nonorm_64/"
    settings = yaml.safe_load(open(model_paths+"settings.yml", "r"))
    print("\nStart calculating the ECFP4 from SMILES:")
    ecfp4,index_error=get_fingerprints_user(data, label= args.smiles)


    if args.model == "aux":
        model = MLP(settings["aux_model"]["layers"],1 ,settings["aux_model"]["dropout"])
        model.load_state_dict(torch.load(model_paths +"aux_cv0.pt", map_location=torch.device('cpu')))
        model.eval()
    # elif args.model == "base":
    #     model = MLP(settings["baseline_model"]["layers"],1 ,settings["baseline_model"]["dropout"])
    #     model.load_state_dict(torch.load(model_paths +"baseline_cv0.pt", map_location=torch.device('cpu')))
    #     model.eval()
    # elif args.model == "ae":
    #     model = FP_AE(settings["ae_model"]["layers"],1+settings["ae_model"]["with_npl"],settings["ae_model"]["dropout"])
    #     model.load_state_dict(torch.load(model_paths +"ae_cv0.pt", map_location=torch.device('cpu')))
    #     model.eval()

    print("\nStart calculating the NPFP from ECFP4:")
    _, npl, nnfp = model(torch.tensor(ecfp4.values, dtype= torch.float))
    nnfp = nnfp.detach().clone().numpy()
    nnfp[index_error,:] = np.nan
    nnfp = pd.DataFrame(nnfp)

    npl = npl[:,[0]].detach().clone().numpy()
    npl[index_error,:] = np.nan
    npl= pd.DataFrame(npl)
    npl.columns= ["nn_naturalproductscore"]


    out=pd.concat([data.iloc[:,args.smiles], npl,nnfp], axis=1)
    #out.columns[1] = "nn_naturalproductscore"
    #output_path="/".join(args.input.split("/")[:-1])
    
    # Remove the smile columns
    out= out.drop(out.columns[:1], axis=1)
    print("Finished!")
    return out.values
    #out.to_csv(output_path+"/"+str(args.model) + "_npfp_"+ time.strftime("%Y%m%d-%H%M%S")+".csv", index=False)


# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
def my_model(smiles_list):
    return fingerprints(smiles_list)


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["nn_naturalproductscore"])  # header
    for o in outputs:
        writer.writerow(o)









  
