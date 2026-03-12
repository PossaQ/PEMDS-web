import pefile
import pandas as pd
import argparse
import os

# Define the feature columns from your dataset (excluding 'Name' and 'Malware' for new EXE predictions)
FEATURE_COLUMNS = [
    'e_magic', 'e_cblp', 'e_cp', 'e_crlc', 'e_cparhdr', 'e_minalloc', 'e_maxalloc', 'e_ss', 'e_sp', 'e_csum',
    'e_ip', 'e_cs', 'e_lfarlc', 'e_ovno', 'e_oemid', 'e_oeminfo', 'e_lfanew', 'Machine', 'NumberOfSections',
    'TimeDateStamp', 'PointerToSymbolTable', 'NumberOfSymbols', 'SizeOfOptionalHeader', 'Characteristics',
    'Magic', 'MajorLinkerVersion', 'MinorLinkerVersion', 'SizeOfCode', 'SizeOfInitializedData',
    'SizeOfUninitializedData', 'AddressOfEntryPoint', 'BaseOfCode', 'ImageBase', 'SectionAlignment',
    'FileAlignment', 'MajorOperatingSystemVersion', 'MinorOperatingSystemVersion', 'MajorImageVersion',
    'MinorImageVersion', 'MajorSubsystemVersion', 'MinorSubsystemVersion', 'SizeOfHeaders', 'CheckSum',
    'SizeOfImage', 'Subsystem', 'DllCharacteristics', 'SizeOfStackReserve', 'SizeOfStackCommit',
    'SizeOfHeapReserve', 'SizeOfHeapCommit', 'LoaderFlags', 'NumberOfRvaAndSizes',
    'SuspiciousImportFunctions', 'SuspiciousNameSection', 'SectionsLength', 'SectionMinEntropy',
    'SectionMaxEntropy', 'SectionMinRawsize', 'SectionMaxRawsize', 'SectionMinVirtualsize',
    'SectionMaxVirtualsize', 'SectionMaxPhysical', 'SectionMinPhysical', 'SectionMaxVirtual',
    'SectionMinVirtual', 'SectionMaxPointerData', 'SectionMinPointerData', 'SectionMaxChar',
    'SectionMainChar', 'DirectoryEntryImport', 'DirectoryEntryImportSize', 'DirectoryEntryExport',
    'ImageDirectoryEntryExport', 'ImageDirectoryEntryImport', 'ImageDirectoryEntryResource',
    'ImageDirectoryEntryException', 'ImageDirectoryEntrySecurity'
]

def extract_pe_features(exe_path):
    try:
        pe = pefile.PE(exe_path)
    except Exception as e:
        raise ValueError(f"Error parsing EXE: {e}")
    
    # Extract DOS header features
    dos_header = {
        'e_magic': pe.DOS_HEADER.e_magic,
        'e_cblp': pe.DOS_HEADER.e_cblp,
        'e_cp': pe.DOS_HEADER.e_cp,
        'e_crlc': pe.DOS_HEADER.e_crlc,
        'e_cparhdr': pe.DOS_HEADER.e_cparhdr,
        'e_minalloc': pe.DOS_HEADER.e_minalloc,
        'e_maxalloc': pe.DOS_HEADER.e_maxalloc,
        'e_ss': pe.DOS_HEADER.e_ss,
        'e_sp': pe.DOS_HEADER.e_sp,
        'e_csum': pe.DOS_HEADER.e_csum,
        'e_ip': pe.DOS_HEADER.e_ip,
        'e_cs': pe.DOS_HEADER.e_cs,
        'e_lfarlc': pe.DOS_HEADER.e_lfarlc,
        'e_ovno': pe.DOS_HEADER.e_ovno,
        'e_oemid': pe.DOS_HEADER.e_oemid,
        'e_oeminfo': pe.DOS_HEADER.e_oeminfo,
        'e_lfanew': pe.DOS_HEADER.e_lfanew
    }
    
    # Extract NT/File header features
    nt_header = {
        'Machine': pe.FILE_HEADER.Machine,
        'NumberOfSections': pe.FILE_HEADER.NumberOfSections,
        'TimeDateStamp': pe.FILE_HEADER.TimeDateStamp,
        'PointerToSymbolTable': pe.FILE_HEADER.PointerToSymbolTable,
        'NumberOfSymbols': pe.FILE_HEADER.NumberOfSymbols,
        'SizeOfOptionalHeader': pe.FILE_HEADER.SizeOfOptionalHeader,
        'Characteristics': pe.FILE_HEADER.Characteristics
    }
    
    # Extract Optional header features
    optional_header = {
        'Magic': pe.OPTIONAL_HEADER.Magic,
        'MajorLinkerVersion': pe.OPTIONAL_HEADER.MajorLinkerVersion,
        'MinorLinkerVersion': pe.OPTIONAL_HEADER.MinorLinkerVersion,
        'SizeOfCode': pe.OPTIONAL_HEADER.SizeOfCode,
        'SizeOfInitializedData': pe.OPTIONAL_HEADER.SizeOfInitializedData,
        'SizeOfUninitializedData': pe.OPTIONAL_HEADER.SizeOfUninitializedData,
        'AddressOfEntryPoint': pe.OPTIONAL_HEADER.AddressOfEntryPoint,
        'BaseOfCode': pe.OPTIONAL_HEADER.BaseOfCode,
        'ImageBase': pe.OPTIONAL_HEADER.ImageBase,
        'SectionAlignment': pe.OPTIONAL_HEADER.SectionAlignment,
        'FileAlignment': pe.OPTIONAL_HEADER.FileAlignment,
        'MajorOperatingSystemVersion': pe.OPTIONAL_HEADER.MajorOperatingSystemVersion,
        'MinorOperatingSystemVersion': pe.OPTIONAL_HEADER.MinorOperatingSystemVersion,
        'MajorImageVersion': pe.OPTIONAL_HEADER.MajorImageVersion,
        'MinorImageVersion': pe.OPTIONAL_HEADER.MinorImageVersion,
        'MajorSubsystemVersion': pe.OPTIONAL_HEADER.MajorSubsystemVersion,
        'MinorSubsystemVersion': pe.OPTIONAL_HEADER.MinorSubsystemVersion,
        'SizeOfHeaders': pe.OPTIONAL_HEADER.SizeOfHeaders,
        'CheckSum': pe.OPTIONAL_HEADER.CheckSum,
        'SizeOfImage': pe.OPTIONAL_HEADER.SizeOfImage,
        'Subsystem': pe.OPTIONAL_HEADER.Subsystem,
        'DllCharacteristics': pe.OPTIONAL_HEADER.DllCharacteristics,
        'SizeOfStackReserve': pe.OPTIONAL_HEADER.SizeOfStackReserve,
        'SizeOfStackCommit': pe.OPTIONAL_HEADER.SizeOfStackCommit,
        'SizeOfHeapReserve': pe.OPTIONAL_HEADER.SizeOfHeapReserve,
        'SizeOfHeapCommit': pe.OPTIONAL_HEADER.SizeOfHeapCommit,
        'LoaderFlags': pe.OPTIONAL_HEADER.LoaderFlags,
        'NumberOfRvaAndSizes': pe.OPTIONAL_HEADER.NumberOfRvaAndSizes
    }
    
    # Extract section-based features (aggregate min/max/length/etc.)
    sections = pe.sections
    sections_length = len(sections)
    section_entropies = [section.get_entropy() for section in sections]
    section_raw_sizes = [section.SizeOfRawData for section in sections]
    section_virtual_sizes = [section.Misc_VirtualSize for section in sections]
    section_physical = [section.Misc_PhysicalAddress for section in sections]
    section_virtual = [section.Misc for section in sections]
    section_pointer_data = [section.PointerToRawData for section in sections]
    section_chars = [section.Characteristics for section in sections]
    
    section_features = {
        'SectionsLength': sections_length,
        'SectionMinEntropy': min(section_entropies) if sections else 0,
        'SectionMaxEntropy': max(section_entropies) if sections else 0,
        'SectionMinRawsize': min(section_raw_sizes) if sections else 0,
        'SectionMaxRawsize': max(section_raw_sizes) if sections else 0,
        'SectionMinVirtualsize': min(section_virtual_sizes) if sections else 0,
        'SectionMaxVirtualsize': max(section_virtual_sizes) if sections else 0,
        'SectionMaxPhysical': max(section_physical) if sections else 0,
        'SectionMinPhysical': min(section_physical) if sections else 0,
        'SectionMaxVirtual': max(section_virtual) if sections else 0,
        'SectionMinVirtual': min(section_virtual) if sections else 0,
        'SectionMaxPointerData': max(section_pointer_data) if sections else 0,
        'SectionMinPointerData': min(section_pointer_data) if sections else 0,
        'SectionMaxChar': max(section_chars) if sections else 0,
        'SectionMainChar': section_chars[0] if sections else 0  # Assuming first section as 'main'
    }
    
    # Extract directory/import/export features
    imports = [imp.dll for imp in pe.DIRECTORY_ENTRY_IMPORT] if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT') else []
    directory_features = {
        'DirectoryEntryImport': len(imports),
        'DirectoryEntryImportSize': sum(len(imp.imports) for imp in pe.DIRECTORY_ENTRY_IMPORT) if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT') else 0,
        'DirectoryEntryExport': len(pe.DIRECTORY_ENTRY_EXPORT.symbols) if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT') else 0,
        'ImageDirectoryEntryExport': pe.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXPORT']].VirtualAddress,
        'ImageDirectoryEntryImport': pe.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT']].VirtualAddress,
        'ImageDirectoryEntryResource': pe.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_RESOURCE']].VirtualAddress,
        'ImageDirectoryEntryException': pe.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXCEPTION']].VirtualAddress,
        'ImageDirectoryEntrySecurity': pe.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_SECURITY']].VirtualAddress,
        'SuspiciousImportFunctions': sum(1 for imp in pe.DIRECTORY_ENTRY_IMPORT for func in imp.imports if func.name and b'suspicious' in func.name.lower()) if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT') else 0,  # Customize 'suspicious' logic
        'SuspiciousNameSection': sum(1 for sec in sections if b'suspicious' in sec.Name.lower())  # Customize logic
    }
    
    # Combine all features into a dict (default to 0 for missing/unsupported)
    all_features = {col: 0 for col in FEATURE_COLUMNS}
    all_features.update(dos_header)
    all_features.update(nt_header)
    all_features.update(optional_header)
    all_features.update(section_features)
    all_features.update(directory_features)
    
    return all_features

def main():
    parser = argparse.ArgumentParser(description="Extract PE features from EXE to CSV for malware detection.")
    parser.add_argument("input_exe", type=str, help="Path to input EXE file")
    parser.add_argument("output_csv", type=str, help="Path to output CSV file")
    args = parser.parse_args()
    
    if not os.path.exists(args.input_exe):
        print(f"Error: Input EXE not found at {args.input_exe}")
        return
    
    features = extract_pe_features(args.input_exe)
    df = pd.DataFrame([features])  # Single row for one EXE
    df.to_csv(args.output_csv, index=False)
    print(f"Features extracted to {args.output_csv}")

if __name__ == "__main__":
    main()