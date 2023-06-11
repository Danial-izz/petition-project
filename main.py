from src.transform import transform

def main():
    #Input files
    input_file = 'data/input_data.json'
    #Call the transform module
    output_df = transform(input_file)
    
    output_file_path = 'output.csv'  # Specify the path and filename for the output CSV file
    #save file into csv, index = False as the Unique identifier would act as the index. Feel free to change the code otherwise
    output_df.to_csv(output_file_path, index=False)
    print(f"Output file saved as {output_file_path}")

if __name__ == '__main__':
    main()